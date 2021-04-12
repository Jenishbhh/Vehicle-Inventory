
import firebase_admin
from firebase_admin import firestore 
from firebase_admin import credentials

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db=firestore.client()

f=('200,4,5')
data={'name': f}

db.collection('User Info').document(f).collection(f).document(f).set(data)