import json

from EnglishModels import *
from ExampleResponse import *
from PydanticModels import Root, run_pydantic
import firebase_admin
from firebase_admin import firestore, credentials

root_model: Root = run_pydantic(json.dumps(api_response), Root)

companies = list(map(lambda item: item.angebot.bildungsanbieter, root_model.embedded["termine"]))
vendorRating = list(map(lambda item: item.anbieterbewertung, root_model.embedded["termine"]))
systematics = list(map(lambda item: item.angebot.systematiken, root_model.embedded["termine"]))
dates = list(map(lambda item: item.aktualisierungsdatum, root_model.embedded["termine"]))
offerers = list(map(lambda item: item.name, root_model.aggregations.ANBIETER.values()))

offerers_no_dups = list(dict.fromkeys(offerers))

trainings = to_trainings(root_model)

print()
print(f"trainings: {trainings.__len__()}")

# Use a service account.
cred = credentials.Certificate('firebaseKey.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()
collection_ref = db.collection("Trainings")

for training in trainings:
    print(training)
    print()
    rval = collection_ref.document(str(training.id)).set(training.model_dump())
    print(rval)
    print()
