#!/usr/bin/env python
import urllib
import json
import os


import cce
import defense_certs
import management
import incident_certs
import pentest_certs
import cd_certs
import encase

from flask import Flask
from flask import request
from flask import make_response



# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = processRequest(req)

    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

@app.route('/webhook', methods=['POST'])
def webhook2():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = processRequest(req)

    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

# Handles different webhooks
def processRequest(req):
    print("Request:")
    print(json.dumps(req, indent=4))

    if req.get("result").get("action") == "input.welcome":
        data = req
        res = getStarted(data)
    elif req.get("result").get("action") == "degree":
        data = req
        res = webhookForDegree(data)
    elif req.get("result").get("action") == "masters":
        data = req
        res = webhookForMaster(data)
    elif req.get("result").get("action") == "beginner":
        data = req
        res = webhook_for_beginner(data)
    elif req.get("result").get("action") == "experienced":
        data = req
        res = webhook_for_experienced(data)
    elif req.get("result").get("action") == "defn-cf":
        data = req
        res = webhook_defn_cf(data)
    elif req.get("result").get("action") == "GIAC-info":
        data = req
        res = webhook_giac_summary(data)
    elif req.get("result").get("action") == "GIAC-cat":
        data = req
        res = webhook_giac_cat(data)
    elif req.get("result").get("action") == "GIAC-pricing":
        data = req
        res = giac_pricing(data)
    elif req.get("result").get("action") == "GIAC-expire":
        data = req
        res = giac_expire(data)
    elif req.get("result").get("action") == "cce-info":
        data = req
        res = cce.webhook_cce_info(data)

    # Statements for EnCase certifications
    elif req.get("result").get("action") == "encase-info":
        data = req
        res = encase.webhook_encase_info(data)
    elif req.get("result").get("action") == "encase-ence":
        data = req
        res = encase.webhook_encase_ence(data)
    elif req.get("result").get("action") == "encase-ence-start":
        data = req
        res = encase.webhook_encase_ence_start(data)
    elif req.get("result").get("action") == "encase-ence-apply":
        data = req
        res = encase.webhook_encase_ence_apply(data)
    elif req.get("result").get("action") == "encase-ence-renew":
        data = req
        res = encase.webhook_encase_ence_renew(data)
    elif req.get("result").get("action") == "encase-cfsr":
        data = req
        res = encase.webhook_encase_cfsr(data)
    elif req.get("result").get("action") == "encase-cfsr-start":
        data = req
        res = encase.webhook_encase_cfsr_start(data)
    elif req.get("result").get("action") == "encase-cfsr-apply":
        data = req
        res = encase.webhook_encase_cfsr_apply(data)
    elif req.get("result").get("action") == "encase-cfsr-renew":
        data = req
        res = encase.webhook_encase_cfsr_renew(data)
    elif req.get("result").get("action") == "encase-encep":
        data = req
        res = encase.webhook_encase_encep(data)
    elif req.get("result").get("action") == "encase-encep-start":
        data = req
        res = encase.webhook_encase_encep_start(data)
    elif req.get("result").get("action") == "encase-encep-apply":
        data = req
        res = encase.webhook_encase_encep_apply(data)
    elif req.get("result").get("action") == "encase-encep-renew":
        data = req
        res = encase.webhook_encase_encep_renew(data)

    # Statements for CCE certification
    elif req.get("result").get("action") == "cce-training":
        data = req
        res = cce.webhook_cce_training(data)
    elif req.get("result").get("action") == "cce-requirements":
        data = req
        res = cce.webhook_cce_requirements(data)
    elif req.get("result").get("action") == "cce-software":
        data = req
        res = cce.webhook_cce_software(data)
    elif req.get("result").get("action") == "cce-fees":
        data = req
        res = cce.webhook_cce_fees(data)
    elif req.get("result").get("action") == "cce-application":
        data = req
        res = cce.webhook_cce_application(data)
    elif req.get("result").get("action") == "cce-testing":
        data = req
        res = cce.webhook_cce_testing(data)

    # Statements for Cyber Defense certifications and training courses need to obtain certification
    elif req.get("result").get("action") == "GIAC-cyber-defense":
        data = req
        res = cd_certs.webhook_giac_cyber_defense(data)
    elif req.get("result").get("action") == "GIAC-cyber-defense-defn":
        data = req
        res = cd_certs.webhook_defn_cd(data)
    elif req.get("result").get("action") == "GIAC-gsec":
        data = req
        res = cd_certs.webhook_giac_gsec(data)
    elif req.get("result").get("action") == "GIAC-sec401":
        data = req
        res = cd_certs.webhook_giac_sec401(data)
    elif req.get("result").get("action") == "GIAC-sec401-syllabus":
        data = req
        res = cd_certs.webhook_giac_sec401_syllabus(data)
    elif req.get("result").get("action") == "GIAC-laptop":
        data = req
        res = cd_certs.webhook_giac_laptop(data)
    elif req.get("result").get("action") == "GIAC-attend":
        data = req
        res = cd_certs.webhook_giac_attend(data)
    elif req.get("result").get("action") == "GIAC-register":
        data = req
        res = cd_certs.webhook_giac_register(data)
    elif req.get("result").get("action") == "GIAC-gcia":
        data = req
        res = cd_certs.webhook_giac_gcia(data)
    elif req.get("result").get("action") == "GIAC-sec503":
        data = req
        res = cd_certs.webhook_giac_sec503(data)
    elif req.get("result").get("action") == "GIAC-sec503-syllabus":
        data = req
        res = cd_certs.webhook_giac_sec503_syllabus(data)
    elif req.get("result").get("action") == "GIAC-gisf":
        data = req
        res = cd_certs.webhook_giac_gisf(data)
    elif req.get("result").get("action") == "GIAC-sec301":
        data = req
        res = cd_certs.webhook_giac_sec301(data)
    elif req.get("result").get("action") == "GIAC-sec301-syllabus":
        data = req
        res = cd_certs.webhook_giac_sec301_syllabus(data)
    
    
    # Statements for Penetration Tester certifications and training courses need to obtain certification
    elif req.get("result").get("action") == "GIAC-pen-tester":
        data = req
        res = pentest_certs.webhook_giac_pen_tester(data)
    elif req.get("result").get("action") == "defn-pen-test":
        data = req
        res = pentest_certs.webhook_defn_pen_test(data)
    elif req.get("result").get("action") == "GIAC-gcih":
        data = req
        res = pentest_certs.webhook_giac_gcih(data)
    elif req.get("result").get("action") == "GIAC-sec504":
        data = req
        res = pentest_certs.webhook_giac_sec504(data)
    elif req.get("result").get("action") == "GIAC-sec504-syllabus":
        data = req
        res = pentest_certs.webhook_giac_sec504_syllabus(data)
    elif req.get("result").get("action") == "GIAC-gpen":
        data = req
        res = pentest_certs.webhook_giac_gpen(data)
    elif req.get("result").get("action") == "GIAC-sec560":
        data = req
        res = pentest_certs.webhook_giac_sec560(data)
    elif req.get("result").get("action") == "GIAC-sec560-syllabus":
        data = req
        res = pentest_certs.webhook_giac_sec560_syllabus(data)
    elif req.get("result").get("action") == "GIAC-gwapt":
        data = req
        res = pentest_certs.webhook_giac_gwapt(data)
    elif req.get("result").get("action") == "GIAC-sec542":
        data = req
        res = pentest_certs.webhook_giac_sec542(data)
    elif req.get("result").get("action") == "GIAC-sec542-syllabus":
        data = req
        res = pentest_certs.webhook_giac_sec542_syllabus(data)


    # Statements for Incident response certifications and training courses need to obtain certification
    
    # Statements for Management certifications and training courses need to obtain certification
    elif req.get("result").get("action") == "GIAC-management":
        data = req
        res = management.webhook_giac_management(data)
    elif req.get("result").get("action") == "defn-management":
        data = req
        res = management.webhook_defn_management(data)
    elif req.get("result").get("action") == "GIAC-gslc":
        data = req
        res = management.webhook_giac_gslc(data)
    elif req.get("result").get("action") == "GIAC-mgt512":
        data = req
        res = management.webhook_giac_mgt512(data)
    elif req.get("result").get("action") == "GIAC-mgt512-syllabus":
        data = req
        res = management.webhook_giac_mgt512_syllabus(data)
    elif req.get("result").get("action") == "GIAC-gsna":
        data = req
        res = management.webhook_giac_gsna(data)
    elif req.get("result").get("action") == "GIAC-aud507":
        data = req
        res = management.webhook_giac_aud507(data)
    elif req.get("result").get("action") == "GIAC-aud507-syllabus":
        data = req
        res = management.webhook_giac_aud507_syllabus(data)
    elif req.get("result").get("action") == "GIAC-gisp":
        data = req
        res = management.webhook_giac_gisp(data)
    elif req.get("result").get("action") == "GIAC-mgt414":
        data = req
        res = management.webhook_giac_mgt414(data)
    elif req.get("result").get("action") == "GIAC-mgt414-syllabus":
        data = req
        res = management.webhook_giac_mgt414_syllabus(data)

    # Statements for Industrial defense certifications and training courses need to obtain certification
   
    else:
        return {}
    return res

def getStarted(req):
    return{
        "messages": [
        {
          "type": 0,
          "platform": "facebook",
          "speech": "Hi, I am the Computer Forensic Cert Bot helper" \
                    "\n\nI am here to help individuals become more aware of what computer forensics is, " \
                    "and also help users find computer forensic qualifications to suit their needs!" \
                    "\n\nAre you a 'beginner' or an 'experienced' computer forensic analyst?"
        },
        {
          "type": 1,
          "platform": "facebook",
          "title": "Pick one",
          "subtitle": "",
          "buttons": [
            {
              "text": "Beginner",
              "postback": ""
            },
            {
              "text": "Experienced",
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

# Webhook for users looking for Degree were computer forensic software certificates are covered
def webhookForDegree(req):
    return {
        "messages": [
            {
              "type": 1,
              "platform": "facebook",
              "title": "Computer Science & I.T",
              "subtitle": "4 year course that touches on Computer Forensics.",
              "imageUrl": "https://www.heaventreedesign.ie/wp-content/uploads/2017/01/nuig.png",
              "buttons": [
                {
                  "text": "Visit degree website",
                  "postback": "http://www.nuigalway.ie/courses/undergraduate-courses/computer-science-and-information-technology.html"
                }
              ]
            },
            {
              "type": 0,
              "speech": ""
            }
          ]
    }

# Webhook for Masters with computer forensics requested by user
def webhookForMaster(req):
    
    return {
        "messages": [
            {
              "type": 1,
              "platform": "facebook",
              "title": "MSc in Digital Investigation & Forensics",
              "subtitle": "For individuals interested in a masters in Digital Investigation & Forensics",
              "imageUrl": "http://m0.her.ie/wp-content/uploads/2016/09/01205231/DCU-image-1024x831.jpg",
              "buttons": [
                {
                  "text": "Visit masters website",
                  "postback": "http://www.ucd.ie/cci/education/prospective_students/msc_difc.html"
                }
              ]
            },
            {
              "type": 0,
              "speech": ""
            }
          ]
    }

# Webhook for General courses recommended by the system
def webhook_for_beginner(req):

    return {

            "messages": [
            {
              "type": 0,
              "platform": "facebook",
              "speech": "These are some good areas to explore for beginner computer forensic analysts!"
            },
            {
              "type": 1,
              "platform": "facebook",
              "title": "GIAC Certification",
              "subtitle": "Great cert for beginners as no previous experience is needed.",
              "imageUrl": "https://i-secure.bypronto.com/wp-content/uploads/sites/1123/cache/2017/10/GIAC1/3730328696.png",
              "buttons": [
                {
                  "text": "GIAC info",
                  "postback": ""
                },
                {
                  "text": "GIAC website",
                  "postback": "https://www.giac.org/"
                }
              ]
            },
            {
              "type": 1,
              "platform": "facebook",
              "title": "MSc in Digital Investigation & Forensics",
              "subtitle": "For individuals interested in a masters in Digital Investigation & Forensics",
              "imageUrl": "http://m0.her.ie/wp-content/uploads/2016/09/01205231/DCU-image-1024x831.jpg",
              "buttons": [
                {
                  "text": "Visit masters website",
                  "postback": "http://www.ucd.ie/cci/education/prospective_students/msc_difc.html"
                }
              ]
            },
            {
              "type": 1,
              "platform": "facebook",
              "title": "Computer Science & I.T",
              "subtitle": "4 year course that touches on Computer Forensics.",
              "imageUrl": "http://src.imu.edu.my/wp-content/uploads/2013/10/nui_galway_brandmark_d_col.png",
              "buttons": [
                {
                  "text": "Visit degree website",
                  "postback": "http://www.nuigalway.ie/courses/undergraduate-courses/computer-science-and-information-technology.html"
                }
              ]
            },
            {
              "type": 1,
              "platform": "facebook",
              "title": "What is computer forensics??",
              "subtitle": "If you are really lost and want to find out more about computer forensics.",
              "imageUrl": "https://katanasecurity.files.wordpress.com/2015/06/cfrs_web_icon.png",
              "buttons": [
                {
                  "text": "Wikipedia",
                  "postback": "https://en.wikipedia.org/wiki/Computer_forensics"
                },
                {
                  "text": "FAQ's Computer Forensics",
                  "postback": "https://evestigate.com/computer-forensics-faq/"
                }
              ]
            },
            {
              "type": 0,
              "speech": ""
            }
          ]
    }



# Webhook for experienced computer forensic examiners looking for certification
def webhook_for_experienced(req):

    return {
        "messages": [
        {
              "type": 0,
              "platform": "facebook",
              "speech": "More advanced computer forensic analysts should look at obtaining Certified Computer Examiner (CCE) certification. " \
                        "\n\nAnother possible option is to get EnCase certification."
        },
        {
            "type": 1,
            "platform": "facebook",
            "title": "CCE certification",
            "subtitle": "If you would like to find out more on CCE certification.",
            "imageUrl": "http://s3.amazonaws.com/s3.timetoast.com/public/uploads/photos/3514969/CCE_LOGO_RGB-1737x17433.png?1360861894",
            "buttons": [
                {
                  "text": "CCE info",
                  "postback": ""
                }
            ]
        },
        {
            "type": 1,
            "platform": "facebook",
            "title": "EnCase certification",
            "subtitle": "If you would like to find out more on Encase certification.",
            "imageUrl": "https://bounga.sg/sites/bounga.sg/files/styles/semi_large__360x360_/public/field/image/ENCE_Logo.png?itok=sg7uh7d3",
            "buttons": [
                {
                  "text": "EnCase info",
                  "postback": ""
                }
            ]
        }
    ]
    }

# Webhook that explains what computer forensics is
def webhook_defn_cf(req):

    return {

    "messages": [
        {
            "type": 1,
            "platform": "facebook",
            "title": "What is computer forensics??",
            "subtitle": "If you are really lost and want to find out more about computer forensics.",
            "imageUrl": "https://katanasecurity.files.wordpress.com/2015/06/cfrs_web_icon.png",
            "buttons": [
                {
                  "text": "Wikipedia",
                  "postback": "https://en.wikipedia.org/wiki/Computer_forensics"
                },
                {
                  "text": "FAQ's Computer Forensics",
                  "postback": "https://evestigate.com/computer-forensics-faq/"
                }
            ]
        }
    ]
    }
    


# ------------------------------------ GIAC SUMMARY -------------------------------------------
def webhook_giac_summary(req):
    
    return {
        "messages": [
        {
          "type": 0,
          "platform": "facebook",
          "speech": "GIAC certifications are for professionals working or interested in information security, " \
                    "legal and law enforcement industries with a need to understand computer " \
                    "forensic analysis. \n\nThe certification focuses on analyzing data from Windows " \
                    "computer systems. \n\n For more info on GIAC's variety of certifications, continue below:"
        },
        {
          "type": 1,
          "platform": "facebook",
          "title": "Further Info",
          "buttons": [
            {
              "text": "GIAC cert categories",
              "postback": ""
            },
            {
              "text": "GIAC website",
              "postback": "https://www.giac.org/certifications"
            },
            {
              "text": "GIAC cert pricing",
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

# GIAC categories of courses
def webhook_giac_cat(req):
    
    return {
        "messages": [
        {
          "type": 0,
          "platform": "facebook",
          "speech": "\nBelow is a list of the most popular sectors that individuals get certified." \
                    "\n\nFor more info on these sectors/categories visit: https://www.giac.org/certifications "
        },
        {
          "type": 1,
          "platform": "facebook",
          "title": "GIAC",
          "subtitle": "Cert categories",
          "imageUrl": "",
          "buttons": [
            {
              "text": "Cyber defense",
              "postback": ""
            },
            {
              "text": "Pen Test",
              "postback": ""
            },
            {
              "text": "Management",
              "postback": ""
            }
          ]
        },
        {
          "type": 1,
          "platform": "facebook",
          "title": "Useful info",
          "subtitle": "What are these things?",
          "imageUrl": "",
          "buttons": [
            {
              "text": "Defn Cyber defense?",
              "postback": ""
            },
            {
              "text": "Defn Pen Test?",
              "postback": ""
            },
            {
              "text": "Defn Management?",
              "postback": ""
            }
          ]
        },
        {
          "type": 1,
          "platform": "facebook",
          "title": "Popular certs",
          "subtitle": "GCFE - Certified Forensic Examiner\nGCFA - Certified Forensic Analyst",
          "imageUrl": "",
          "buttons": [
            {
              "text": "GCFE",
              "postback": ""
            },
            {
              "text": "GCFA",
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

def giac_pricing(req):

  return{

    "messages": [
        {
          "type": 0,
          "platform": "facebook",
          "speech": "\nGiac Certification Pricing is listed below:" \
                    "\n\nGIAC Certification Attempt -         $1,699" \
                    "\nGIAC Gold Certification -              $529" \
                    "\n(GSE) Hands-on Lab Fee -             $2,309" \
                    "\n(GSE) Multiple Choice Exam -        $449" \
                    "\nCertification Attempt Extensions - $379" \
                    "\nCertification Renewal -            $429" \
        },
        {
          "type": 1,
          "platform": "facebook",
          "title": "Cert expiration",
          "subtitle": "When will this certification expire?",
          "imageUrl": "",
          "buttons": [
            {
              "text": "GIAC expire",
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

def giac_expire(req):

  return{

      "messages": [
        {
          "type": 0,
          "platform": "facebook",
          "speech": "Each GIAC certification remains valid for 4 years." \
                    " The first 2 years you are certified require no further action from you." \
                    " After 2 years, the certification renewal process will begin, " \
                    "with the ultimate goal being that you have demonstrated ongoing competency in the Information " \
        },
        {
          "type": 0,
          "speech": ""
        }
      ]
  }

if __name__ == '__main__' :
    port = int(os.getenv('PORT', 80))
    print ("Starting app on port %d" %(port))
    app.run(debug=True, port=port, host='0.0.0.0')
