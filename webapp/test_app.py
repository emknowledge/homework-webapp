import unittest
from app import app

class RouteTests(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()

    def tearDown(self):
        pass    

    def test_root(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_create(self):
        response = self.app.get('/create', follow_redirects=True)   
        self.assertEqual(response.status_code, 200)  

    def test_post(self):
        response = self.app.get('//post_id', follow_redirects=True)   
        self.assertEqual(response.status_code, 200) 

    def test_edit(self):
        response = self.app.get('//edit', follow_redirects=True)   
        self.assertEqual(response.status_code, 200)   

    def test_delete(self):
        response = self.app.get('//delete', follow_redirects=True)   
        self.assertEqual(response.status_code, 200)            

if __name__=="__main__":
    unittest.main()