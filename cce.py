#----------------- Certified Computer Examiner (CCE) -----------------------------
def webhook_cce_info(req):
    
    return {
        "messages": [
        {
          "type": 0,
          "platform": "facebook",
          "speech": "The purpose of CCE certification is to certify computer forensic examiners solely " \
             "based on their knowledge and practical examination skills and abilities as they relate " \
             "to the practice of digital forensics. Because of its high forensic and ethical standards, " \
             "the CCE has evolved into one of the most desired certifications in the digital forensics industry."
        },
        {
          "type": 1,
          "platform": "facebook",
          "title": "Useful links",
          "buttons": [
            {
              "text": "CCE Application",
              "postback": "https://www.isfce.com/app.html"
            },
            {
              "text": "CCE Software",
              "postback": "https://www.isfce.com/software.htm"
            },
            {
              "text": "CCE Website",
              "postback": "https://www.isfce.com/certification.htm"
            }
          ]
        },
        {
          "type": 1,
          "platform": "facebook",
          "title": "Useful info",
          "buttons": [
            {
              "text": "CCE Requirements",
              "postback": ""
            },
            {
              "text": "CCE Fees",
              "postback": ""
            },
            {
              "text": "CCE Training",
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

def webhook_cce_training(req):

    return {
       "messages": [
        {
          "type": 0,
          "platform": "facebook",
          "speech": "The ISFCE has Authorized Training Centers (ATCs) around the world to train specifically for CCE certification. " \
                    "It is reccommended that you enroll within one of these courses before " \
                    "attempting the CCE certification testing."
        },
        {
          "type": 1,
          "platform": "facebook",
          "title": "Bootcamp",
          "buttons": [
            {
              "text": "ATC's Website",
              "postback": "http://www.cce-bootcamp.com/"
            }
          ]
        },
        {
          "type": 0,
          "speech": ""
        }
      ]
    }

def webhook_cce_requirements(req):
    
    return {
        "messages": [
        {
          "type": 0,
          "platform": "facebook",
          "speech": "CCE Requirements:" \
                    "\nComplete training at a CCE Bootcamp Authorized Training Center" \
                    "\n--------------OR----------------" \
                    "\nMinimum of 18 months of professional experience conducting digital forensic examinations" \
                    "\n--------------OR----------------" \
                    "\nHave documented self study in the field of digital forensics" 
        },
        {
          "type": 1,
          "platform": "facebook",
          "title": "Extra info",
          "buttons": [
            {
              "text": "CCE Requirements site",
              "postback": "https://www.isfce.com/requirements.htm"
            }
          ]
        },
        {
          "type": 0,
          "speech": ""
        }
      ]
    }



def webhook_cce_fees(req):
    
    speech = "CCE Fees - $395.00 USD" \
             "\n\nCCE Recertification (2 years) - $75.00 USD" \
             "\n\nRetake the CCE Exam - $175.00 USD" \
             "\n\nVisit the CCE website for more info on their fees at: https://www.isfce.com/fee.htm " \

    print("Response")
    print(speech)
    return {
        "messages": [
        {
          "type": 0,
          "platform": "facebook",
          "speech": "CCE Fees - $395.00 USD" \
             "\n\nCCE Recertification (2 years) - $75.00 USD" \
             "\n\nRetake the CCE Exam - $175.00 USD" \
        },
        {
          "type": 1,
          "platform": "facebook",
          "title": "Extra info",
          "buttons": [
            {
              "text": "CCE Fees site",
              "postback": "https://www.isfce.com/fee.htm"
            }
          ]
        },
        {
          "type": 0,
          "speech": ""
        }
      ]
    }

