import json

from EnglishModels import *
from ExampleResponse import *
from PydanticModels import Root, run_pydantic, TrainingsProvider
import firebase_admin
from firebase_admin import firestore, credentials

root_model: Root = run_pydantic(json.dumps(api_response), Root)

companies: List[TrainingsProvider] = [item.angebot.bildungsanbieter for item in root_model.embedded["termine"]]

trainings = to_trainings(root_model)
companies_details = to_training_provider(companies, trainings)

print()
print(f"trainings: {trainings.__len__()}")

# Use a service account.
cred = credentials.Certificate('firebaseKey.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()
collection_ref = db.collection("trainings")

for company in trainings:
    print(company)
    print()
    # rval = collection_ref.document(str(company.id)).set(company.model_dump())
    # print(rval)
    print()
