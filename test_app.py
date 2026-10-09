import os
import tempfile
import unittest
import app as app_module

class IncidentManagerTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        app_module.DB = __import__("pathlib").Path(self.tmp.name) / "test.db"
        app_module.app.config.update(TESTING=True, SECRET_KEY="test")
        app_module.init_db()
        self.client = app_module.app.test_client()

    def tearDown(self):
        self.tmp.cleanup()

    def test_home_and_dashboard(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Incidents ouverts", response.data)

    def test_create_valid_incident(self):
        response = self.client.post("/incidents", data={
            "titre": "Alerte phishing fictive", "description": "Message de démonstration",
            "categorie": "Phishing", "gravite": "Élevée"
        })
        self.assertEqual(response.status_code, 303)
        self.assertIn(b"Alerte phishing fictive", self.client.get("/").data)

    def test_empty_title_rejected(self):
        response = self.client.post("/incidents", data={
            "titre": " ", "description": "", "categorie": "Phishing", "gravite": "Moyenne"
        })
        self.assertEqual(response.status_code, 400)
        with app_module.connect() as db:
            self.assertEqual(db.execute("SELECT COUNT(*) FROM incidents").fetchone()[0], 0)

    def test_unknown_severity_rejected(self):
        response = self.client.post("/incidents", data={
            "titre": "Test", "description": "", "categorie": "Phishing", "gravite": "Extrême"
        })
        self.assertEqual(response.status_code, 400)

    def test_too_long_description_rejected(self):
        response = self.client.post("/incidents", data={
            "titre": "Test", "description": "x" * (app_module.DESCRIPTION_MAX + 1),
            "categorie": "Phishing", "gravite": "Moyenne"
        })
        self.assertEqual(response.status_code, 400)

    def test_invalid_status_rejected(self):
        response = self.client.post("/incidents/1/statut", data={"statut": "Pwned"})
        self.assertEqual(response.status_code, 400)

    def test_filter_by_severity(self):
        self.client.post("/incidents", data={
            "titre": "Critique fictif", "description": "", "categorie": "Compte", "gravite": "Critique"
        })
        response = self.client.get("/?gravite=Critique")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Critique fictif", response.data)
        self.assertNotIn(b"Incident ordinaire", response.data)

    def test_regression_sql_payload_is_data(self):
        payload = "' OR 1=1 --"
        self.client.post("/incidents", data={
            "titre": payload, "description": "", "categorie": "Autre", "gravite": "Faible"
        })
        response = self.client.get("/")
        self.assertIn(payload.encode(), response.data)
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main(verbosity=2)
