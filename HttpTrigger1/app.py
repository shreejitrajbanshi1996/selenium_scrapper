import HttpTrigger1.config
import HttpTrigger1.services
import HttpTrigger1.services.token as token_services
import HttpTrigger1.services.registrations as registrationServices
import HttpTrigger1.services.events as eventServices
import HttpTrigger1.services.eventHostDetails as eventHostDetailsService

def update_registrations(registrations_dynamics, registrations_certain, event_id):

    for certain_registation in registrations_certain:
        found = False

        for dynamcs_registration in registrations_dynamics:
            if certain_registation["Reg Code"] == dynamcs_registration["aiad_registration_code"]:
                found = True

                if certain_registation["Reg Status"] == "2":
                    break

                registrationServices.update(
                    {"aiad_registrationid": dynamcs_registration["aiad_registrationid"],
                     "aiad_status": 273630000
                     })
                break

        if found:
            continue

        registrationServices.create({'aiad_status': 273630000,
                                     'aiad_country': certain_registation['RegistrantCountry'],
                                     'aiad_firstname': certain_registation['First Name'],
                                     'aiad_lastname': certain_registation['Last Name'],
                                     'aiad_jobtitle': certain_registation['Job Title text'],
                                     'aiad_organization': certain_registation['Organization'],
                                     'aiad_email': certain_registation['Email'],
                                     'aiad_phone': certain_registation['Phone'],
                                     'aiad_attendeetype': certain_registation['Attendee Type'],
                                     'aiad_registration_code': certain_registation['Reg Code'],
                                     'aiad_profileuniqueid': certain_registation['Profile Unique Id']
                                     })


def run_scrapper_for_events(username, password, events):

    for event in events:
        registrations_dynamics = registrationServices.get_all_by_event_id(
            event['aiad_eventid'])

        registrations_certain = registrationServices.get_registration_data_from_certain(
            username, password, event['aiad_uniqueregistrationid'])

        update_registrations(registrations_dynamics,
                             registrations_certain, event['aiad_eventid'])


def start_app():
    print("Started program execution")

    token_services.set_token()

    username, password = eventHostDetailsService.get_partner_credential()

    events = eventServices.get_all_valid_events()

    run_scrapper_for_events(username, password, events)


# Module system in python
# Object oriented programming in python
# Async and await function call in python
# Run Crone job in python
# Exception handling in python
# Asyn and Await block in Nodejs and python during network call