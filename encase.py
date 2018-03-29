#----------------- EnCase certification-----------------------------
def webhook_encase_info(req):

    return {
        "messages": [
        {
          "type": 0,
          "platform": "facebook",
          "speech": "The purpose of EnCase certification is proof that individuals possess a deep " \
             "understanding of the EnCase software. The guidance certification program focuses " \
             "on teaching individuals how to recover evidence from seized harddrives." \
             "\n\nThere are currently three certifications offered by EnCase:" \
             "\n1. EnCase Certified Examiner (EnCE)"
             "\n2. Certified Forensic Security Responder (CFSR)"
             "\n3. EnCase Certified eDiscovery Practitioner (EnCEP)"
        },
        {
          "type": 1,
          "platform": "facebook",
          "title": "Certifications",
          "buttons": [
            {
              "text": "EnCE info",
              "postback": ""
            },
            {
              "text": "CFSR info",
              "postback": ""
            },
            {
              "text": "EnCEP info",
              "postback": ""
            }
          ]
        },
        {
          "type": 0,
          "speech": ""
        }
      ]
    }

#----------------------------EnCE-------------------------------------------
def webhook_encase_ence(req):
    
    return {
        "messages": [
        {
          "type": 0,
          "platform": "facebook",
          "speech": "The EnCase Certified Examiner(EnCE) program certifies both public and private sector " \
                    "professionals in the use of Guidance Software's EnCase computer forensic software. " \
                    "Recognized by both the law enforcement and corporate communities as a symbol of a skilled computer examiner."
        },
        {
          "type": 1,
          "platform": "facebook",
          "title": "Useful links",
          "buttons": [
            {
              "text": "EnCE Training",
              "postback": "https://www.guidancesoftware.com/docs/default-source/training/ence-get-started.pdf?sfvrsn=12"
            },
            {
              "text": "EnCE Apply",
              "postback": "https://www.guidancesoftware.com/docs/default-source/training/ence-application.pdf?sfvrsn=2"
            },
            {
              "text": "EnCE Renew",
              "postback": "https://www.guidancesoftware.com/docs/default-source/training/ence-renewal-form.pdf?sfvrsn=2"
            }
          ]
        },
        {
          "type": 0,
          "speech": ""
        }
      ]
    }

#----------------------------CFSR-------------------------------------------

def webhook_encase_cfsr(req):
    
    return {
        "messages": [
        {
          "type": 0,
          "platform": "facebook",
          "speech": "The Certified Forensic Security Responder(CFSR) will equip you with the breadth and depth of " \
                    "knowledge that you need to become a highly sought-after cyber security forensics expert. "
        },
        {
          "type": 1,
          "platform": "facebook",
          "title": "Useful links",
          "buttons": [
            {
              "text": "CFSR Training",
              "postback": "https://www.guidancesoftware.com/docs/default-source/training/cfsr-get-started.pdf?sfvrsn=60918cad_16"
            },
            {
              "text": "CFSR Apply",
              "postback": "https://www.guidancesoftware.com/docs/default-source/training/cfsr-application.pdf?sfvrsn=2"
            },
            {
              "text": "CFSR Renew",
              "postback": "https://www.guidancesoftware.com/docs/default-source/training/cfsr-renewal.pdf?sfvrsn=2"
            }
          ]
        },
        {
          "type": 0,
          "speech": ""
        }
      ]
    }

#----------------------------EnCEP-------------------------------------------

def webhook_encase_encep(req):
    
    return {
        "messages": [
        {
          "type": 0,
          "platform": "facebook",
          "speech": "EnCase Certified eDiscovery Practitioner(EnCEP) program is the leading e-discovery solution for the " \
             "search, collection, preservation, and processing of electronically stored information(ESI). " \
             "Recognized by both the law enforcement and corporate communities as a symbol of a skilled computer examiner. "
        },
        {
          "type": 1,
          "platform": "facebook",
          "title": "Useful links",
          "buttons": [
            {
              "text": "EnCEP Training",
              "postback": "https://www.guidancesoftware.com/docs/default-source/training/encep-get-started.pdf?sfvrsn=6fvrsn=6"
            },
            {
              "text": "EnCEP Apply",
              "postback": "https://www.guidancesoftware.com/docs/default-source/training/encep-application.pdf?sfvrsn=2"
            },
            {
              "text": "EnCEP Renew",
              "postback": "https://www.guidancesoftware.com/docs/default-source/training/encep-renewal-form.pdf?sfvrsn=2"
            }
          ]
        },
        {
          "type": 0,
          "speech": ""
        }
      ]
    }

