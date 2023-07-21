from pydantic import BaseModel, Field, ValidationError
from typing import Optional, List, Dict, Any
from PydanticModels import Root, TrainingsProvider


class Offer(BaseModel):
    id: int
    title: Optional[str]
    content: Optional[str]
    degree_type: Optional[str]
    degree_designation: Optional[str]
    funding: Optional[str]
    access: Optional[str]
    # credits_info: Optional[Any] = None
    additional_qualifications: Optional[Any] = None
    link: Optional[str]
    target_group: Optional[str]
    provider_id: Optional[int]
    education_type: Optional[str]  # Optional[Entity]
    school_type: Optional[str]  # Optional[Entity]
    disabilities: Optional[List[str]]  # Optional[List[Entity]]
    certifier: Optional[Any] = None
    search_terms: List[str]  # Optional[List[Dict[str, str]]]
    offer_type: Optional[str]  # Optional[Entity]


class Street(BaseModel):
    zip_code: Optional[str]
    name: Optional[str]
    country: Optional[str]  # Optional[country]


class Address(BaseModel):
    label: Optional[Any] = None
    street: Optional[str]
    hints: Optional[Any] = None
    placeStreet: Optional[Street]
    lat: Optional[float]  # coordinates.lat: Optional[Coordinates]
    lon: Optional[float]  # coordinates.lon: Optional[Coordinates]


class ContactPerson(BaseModel):
    id: Optional[int]
    salutation: Optional[str]
    title: Optional[str]
    surname: Optional[str]
    first_name: Optional[str]
    phone_area_code: Optional[str]
    phone_extension: Optional[str]
    mobile_area_code: Optional[Any] = None
    mobile_extension: Optional[Any] = None
    faxPrefix: Optional[Any] = None
    faxExtension: Optional[Any] = None
    email: Optional[str]
    homepage: Optional[str]
    role: List[str]  # Optional[List[Entity]]


class Training(BaseModel):
    id: Optional[int]
    lesson_type: Optional[str]  # Optional[Entity]
    class_time: Optional[str]  # Optional[Entity]
    duration: Optional[str]  # Optional[Entity]
    vendor_evaluation: Optional[Any] = None
    offer: Optional[Offer]
    address: Optional[Address]
    lesson_times: Optional[str]
    other_teaching_form: Optional[Any] = None
    cost_value: Optional[Any] = None
    costCurrency: Optional[str]
    costRemark: Optional[str]
    funding: Optional[bool]
    link: Optional[str]
    remark: Optional[Any] = None
    beginning: Optional[int]
    end: Optional[int]
    individual_entry: Optional[bool]
    registration_deadline: Optional[int]
    remarkTime: Optional[str]
    participantMin: Optional[Any] = None
    participantMax: Optional[Any] = None
    update_date: Optional[int]
    event_flows: Optional[List[Any]] = []
    checking_location: Optional[Any] = None
    own_offer_number: Optional[Any] = None
    in_house_company_seminar: Optional[bool]
    extra_occupational: Optional[bool]
    practice_parts: Optional[bool]
    contact_persons: Optional[List[ContactPerson]]


class CompanyDetails(BaseModel):
    id: Optional[int]
    name: Optional[str]
    # description: Optional[str]
    trainings: List[int]  # Training ids
    phoneAreaCode: Optional[str]
    phoneExtension: Optional[str]
    mobileAreaCode: Optional[Any] = None
    mobileExtension: Any = None
    faxPrefix: Any = None
    faxExtension: Any = None
    homepage: Optional[str]
    email: Optional[str]
    address: Address
    logo_url: Optional[str]  # Logo.externalUrl


def to_trainings(root_model: Root) -> List[Training]:
    return list(
        map(
            lambda item:
            Training(
                id=item.id,
                lesson_type=item.unterrichtsform.bezeichnung,
                class_time=item.unterrichtszeit.bezeichnung,
                duration=item.dauer.bezeichnung,
                vendor_evaluation=item.anbieterbewertung,
                offer=Offer(
                    id=item.angebot.id,
                    title=item.angebot.titel,
                    content=item.angebot.inhalt,
                    degree_type=item.angebot.abschlussart,
                    degree_designation=item.angebot.abschlussbezeichnung,
                    funding=item.angebot.foerderung,
                    access=item.angebot.zugang,
                    additional_qualifications=item.angebot.zusatzqualifikationen,
                    link=item.angebot.link,
                    target_group=item.angebot.zielgruppe,
                    provider_id=item.angebot.bildungsanbieter.id,
                    education_type=item.angebot.bildungsart.bezeichnung,
                    school_type=item.angebot.schulart.bezeichnung,
                    disabilities=list(map(lambda dis: dis.bezeichnung, item.angebot.behinderungen)),
                    certifier=item.angebot.zertifizierer,
                    search_terms=[value for term_dict in item.angebot.suchworte for value in term_dict.values()],
                    offer_type=item.angebot.angebotstyp.bezeichnung
                ),
                address=Address(
                    label=item.adresse.bezeichnung,
                    street=item.adresse.strasse,
                    hints=item.adresse.hinweise,
                    placeStreet=Street(
                        zip_code=item.adresse.ortStrasse.plz,
                        name=item.adresse.ortStrasse.name,
                        country=item.adresse.ortStrasse.land.name
                    ),
                    lat=item.adresse.koordinaten.lat,
                    lon=item.adresse.koordinaten.lon
                ),
                lesson_times=item.unterrichtszeiten,
                other_teaching_form=item.sonstigeUnterrichtsform,
                cost_value=item.kostenWert,
                costCurrency=item.kostenWaehrung,
                costRemark=item.kostenBemerkung,
                funding=item.foerderung,
                link=item.link,
                remark=item.bemerkung,
                beginning=item.beginn,
                end=item.ende,
                individual_entry=item.individuellerEinstieg,
                registration_deadline=item.anmeldeschluss,
                remarkTime=item.bemerkungZeit,
                participantMin=item.teilnehmerMin,
                participantMax=item.teilnehmerMax,
                update_date=item.aktualisierungsdatum,
                event_flows=item.veranstaltungsablaeufe,
                checking_location=item.pruefendeStelle,
                own_offer_number=item.eigeneAngebotsnummer,
                in_house_company_seminar=item.inhouseFirmenseminar,
                extra_occupational=item.berufsbegleitend,
                practice_parts=item.praxisanteile,
                contact_persons=list(
                    map(lambda person:
                        ContactPerson(
                            id=person.id,
                            salutation=person.anrede,
                            title=person.titel,
                            surname=person.nachname,
                            first_name=person.vorname,
                            phone_area_code=person.telefonVorwahl,
                            phone_extension=person.telefonDurchwahl,
                            mobile_area_code=person.mobilVorwahl,
                            mobile_extension=person.mobilDurchwahl,
                            faxPrefix=person.faxVorwahl,
                            faxExtension=person.faxDurchwahl,
                            email=person.email,
                            homepage=person.homepage,
                            role=list(map(lambda rol: rol.bezeichnung, person.rollen))
                        ),
                        item.ansprechpartner
                        )
                )

            )
            , root_model.embedded["termine"]
        )
    )


def to_training_provider(companies: List[TrainingsProvider], trainings: List[Training]) -> List[CompanyDetails]:
    return list(
        map(
            lambda company:
            CompanyDetails(
                id=company.id,
                name=company.name,
                # description=,
                trainings=[training.id for training in trainings if training.offer.provider_id == company.id],
                # Training ids
                phoneAreaCode=company.telefonVorwahl,
                phoneExtension=company.telefonDurchwahl,
                mobileAreaCode=company.mobilVorwahl,
                mobileExtension=company.mobilDurchwahl,
                faxPrefix=company.faxVorwahl,
                faxExtension=company.faxDurchwahl,
                homepage=company.homepage,
                email=company.email,
                address=Address(
                    label=company.adresse.bezeichnung,
                    street=company.adresse.strasse,
                    hints=company.adresse.hinweise,
                    placeStreet=Street(
                        zip_code=company.adresse.ortStrasse.plz,
                        name=company.adresse.ortStrasse.name,
                        country=company.adresse.ortStrasse.land.name
                    ),
                    lat=company.adresse.koordinaten.lat,
                    lon=company.adresse.koordinaten.lon
                ),
                logo_url=company.logo.externalURL,
            )
            , companies
        )
    )
