from pydantic import BaseModel, Field, ValidationError
from typing import Optional, List, Dict, Any


def run_pydantic(json_data, d_class: BaseModel) -> BaseModel:
    try:
        json_root = d_class.model_validate_json(json_data)
        print(json_root.model_dump_json(indent=4))
        return json_root
    except ValidationError as e:
        print(e.errors())


string_string_dict = {
    "suchwort": "Online"
}

entity_data = {
    "id": 5,
    "bezeichnung": "String"
}


class Entity(BaseModel):
    id: Optional[int]
    bezeichnung: Optional[str]


land_data = {
    "id": 5,
    "name": "String",
    "laenderCode": "String",
    "bundeslandCode": "String",
    "code": "String"
}


class Land(BaseModel):
    id: Optional[int]
    name: Optional[str]
    laenderCode: Optional[str]
    bundeslandCode: Optional[str]
    code: Optional[str]


town_data = {
    "id": 5,
    "plz": "String",
    "name": "String",
    "land": land_data
}


class TownStreet(BaseModel):
    id: Optional[int]
    plz: Optional[str]
    name: Optional[str]
    land: Optional[Land]


coordinates_data = {
    "lat": 0.00,
    "lon": 0.00
}


class Coordinates(BaseModel):
    lat: Optional[float]
    lon: Optional[float]


address_data = {
    "id": 5,
    "bezeichnung": None,
    "strasse": "String",
    # "hinweise": None,
    "ortStrasse": town_data,
    "koordinaten": coordinates_data
}


class Address(BaseModel):
    id: Optional[int]
    bezeichnung: Optional[Any] = None
    strasse: Optional[str]
    hinweise: Optional[Any] = None
    ortStrasse: Optional[TownStreet]
    koordinaten: Optional[Coordinates]


logo_data = {
    "id": 5,
    "url": "String",
    "externalURL": "String"
}


class Logo(BaseModel):
    id: Optional[int]
    url: Optional[str]
    externalURL: Optional[str]


training_provider_data = {
    "id": 5,
    "name": "String",
    "telefonVorwahl": "String",
    "telefonDurchwahl": "String",
    "mobilVorwahl": None,
    "mobilDurchwahl": None,
    "faxVorwahl": None,
    "faxDurchwahl": None,
    "homepage": "String",
    "email": "String",
    "adresse": address_data,
    "logo": logo_data
}


class TrainingsProvider(BaseModel):
    id: Optional[int]
    name: Optional[str]
    telefonVorwahl: Optional[str]
    telefonDurchwahl: Optional[str]
    mobilVorwahl: Optional[Any] = None
    mobilDurchwahl: Optional[Any] = None
    faxVorwahl: Optional[Any] = None
    faxDurchwahl: Optional[Any] = None
    homepage: Optional[str]
    email: Optional[str]
    adresse: Optional[Address]
    logo: Optional[Logo]


systematics_data = {
    "id": 5,
    "codeNr": "string",
    "kurzbezeichnung": None,
    "suchworte": string_string_dict
}


class Systematics(BaseModel):
    id: Optional[int]
    codeNr: Optional[str]
    kurzbezeichnung: Optional[Any] = None
    suchworte: Optional[List[Dict[str, str]]]


angebot_data = {
    "id": 5,
    "titel": "String",
    "inhalt": "String",
    "abschlussart": "String",
    "abschlussbezeichnung": "String",
    "foerderung": "String",
    "zugang": "String",
    "anrechnung": None,
    "berechtigungen": None,
    "zusatzqualifikationen": None,
    "link": "String",
    "zielgruppe": "String",
    "bildungsanbieter": training_provider_data,
    "bildungsart": entity_data,
    "systematiken": [systematics_data],
    "schulart": entity_data,
    "behinderungen": entity_data,
    "zertifizierer": [None],
    "traeger": None,
    "suchworte": [string_string_dict],
    "angebotstyp": entity_data
}


class Angebot(BaseModel):
    id: Optional[int]
    titel: Optional[str]
    inhalt: Optional[str]
    abschlussart: Optional[str]
    abschlussbezeichnung: Optional[str]
    foerderung: Optional[str]
    zugang: Optional[str]
    zusatzqualifikationen: Optional[Any] = None
    link: Optional[str]
    zielgruppe: Optional[str]
    bildungsanbieter: Optional[TrainingsProvider]
    bildungsart: Optional[Entity]
    systematiken: Optional[List[Systematics]]
    schulart: Optional[Entity]
    behinderungen: Optional[List[Entity]]
    zertifizierer: Optional[List[Dict[str, Any]]] = []
    traeger: Optional[Any] = None
    suchworte: Optional[List[Dict[str, str]]]
    angebotstyp: Optional[Entity]


contact_person_data = {
    "id": 5,
    "anrede": "String",
    "titel": "String",
    "nachname": "String",
    "vorname": "String",
    "telefonVorwahl": "String",
    "telefonDurchwahl": "String",
    "mobilVorwahl": None,
    "mobilDurchwahl": None,
    "faxVorwahl": None,
    "faxDurchwahl": None,
    "email": "String",
    "homepage": "String",
    "rollen": [entity_data]
}


class ContactPerson(BaseModel):
    id: Optional[int]
    anrede: Optional[str]
    titel: Optional[str]
    nachname: Optional[str]
    vorname: Optional[str]
    telefonVorwahl: Optional[str]
    telefonDurchwahl: Optional[str]
    mobilVorwahl: Optional[Any] = None
    mobilDurchwahl: Optional[Any] = None
    faxVorwahl: Optional[Any] = None
    faxDurchwahl: Optional[Any] = None
    email: Optional[str]
    homepage: Optional[str]
    rollen: Optional[List[Entity]]


ort_data = {
    "name": "String",
    "postleitzahl": None,
    "laengengrad": 0.00,
    "breitengrad": 0.00
}


class Ort(BaseModel):
    name: Optional[str]
    postleitzahl: Optional[Any] = None
    laengengrad: Optional[float]
    breitengrad: Optional[float]


staying_away_data = {
    "ort": ort_data,
    "abstandInKm": 0.00
}


class StayingAway(BaseModel):
    ort: Optional[Ort]
    abstandInKm: Optional[float]


termine_data = {
    "id": 5,
    "unterrichtsform": entity_data,
    "unterrichtszeit": entity_data,
    "dauer": entity_data,
    "anbieterbewertung": None,
    "angebot": angebot_data,
    "adresse": address_data,
    "unterrichtszeiten": "String",
    "sonstigeUnterrichtsform": None,
    "kostenWert": None,
    "kostenWaehrung": "String",
    "kostenBemerkung": "String",
    "foerderung": True,
    "link": "String",
    "bemerkung": None,
    "beginn": 5,
    "ende": 5,
    "individuellerEinstieg": True,
    "anmeldeschluss": 5,
    "bemerkungZeit": "String",
    "teilnehmerMin": None,
    "teilnehmerMax": None,
    "aktualisierungsdatum": 5,
    "veranstaltungsablaeufe": [None],
    "pruefendeStelle": None,
    "eigeneAngebotsnummer": None,
    "inhouseFirmenseminar": False,
    "berufsbegleitend": False,
    "praxisanteile": False,
    "ansprechpartner": [contact_person_data],
    "rehaBereich": None,
    "abstaende": [staying_away_data]
}


class Termine(BaseModel):
    id: Optional[int]
    unterrichtsform: Optional[Entity]
    unterrichtszeit: Optional[Entity]
    dauer: Optional[Entity]
    anbieterbewertung: Optional[Any] = None
    angebot: Optional[Angebot]
    adresse: Optional[Address]
    unterrichtszeiten: Optional[str]
    sonstigeUnterrichtsform: Optional[Any] = None
    kostenWert: Optional[Any] = None
    kostenWaehrung: Optional[str]
    kostenBemerkung: Optional[str]
    foerderung: Optional[bool]
    link: Optional[str]
    bemerkung: Optional[Any] = None
    beginn: Optional[int]
    ende: Optional[int]
    individuellerEinstieg: Optional[bool]
    anmeldeschluss: Optional[int]
    bemerkungZeit: Optional[str]
    teilnehmerMin: Optional[Any] = None
    teilnehmerMax: Optional[Any] = None
    aktualisierungsdatum: Optional[int]
    veranstaltungsablaeufe: Optional[List[Any]] = []
    pruefendeStelle: Optional[Any] = None
    eigeneAngebotsnummer: Optional[Any] = None
    inhouseFirmenseminar: Optional[bool]
    berufsbegleitend: Optional[bool]
    praxisanteile: Optional[bool]
    ansprechpartner: Optional[List[ContactPerson]]
    rehaBereich: Optional[Any] = None
    abstaende: Optional[List[StayingAway]]


link_data = {
    "href": "String"
}


class Href(BaseModel):
    href: Optional[str]


page_data = {
    "size": 5,
    "totalElements": 5,
    "totalPages": 5,
    "number": 5
}


class Page(BaseModel):
    size: Optional[int]
    totalElements: Optional[int]
    totalPages: Optional[int]
    number: Optional[int]


result_stat_data = {
    "anzahlErgebnisse": 5,
    "name": "String"
}


class ResultStat(BaseModel):
    anzahlErgebnisse: Optional[int]
    name: Optional[str]


start_date_data = {
    "id": 5,
    "name": "String",
    "anzahl": 5
}


class StartDate(BaseModel):
    id: Optional[int]
    name: Optional[str]
    anzahl: Optional[int]


class Aggregations(BaseModel):
    ANZAHL_AUSGEFILTERT: Optional[Dict[str, int]]
    UNTERRICHTSZEIT: Optional[Dict[str, int]]
    INTEGRATION: Optional[Dict]
    UNTERRICHTSFORMEN: Optional[Dict]
    ANBIETER: Optional[Dict[str, ResultStat]]
    BEGINNTERMIN: Optional[Dict[str, StartDate]]
    DAUER: Optional[Dict[str, int]]
    BILDUNGSGUTSCHEIN: Optional[str]
    LERNFORMEN: Optional[Dict[str, Dict[str, int]]]
    REGIONEN: Optional[Dict[str, int]]
    ANZAHL_GESAMT: Optional[Dict[str, int]]


root_data = {
    "_embedded": {
        "termine": [termine_data]
    },
    "_links": {
        "String": link_data
    },
}


class Root(BaseModel):
    embedded: Optional[Dict[str, List[Termine]]] = Field(alias="_embedded")
    links: Optional[Dict[str, Href]] = Field(alias="_links")
    page: Optional[Page]
    aggregations: Optional[Aggregations]

