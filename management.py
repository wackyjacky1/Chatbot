#-------------------------------------------------- GIAC Management, Audit, Legal ---------------------------------------
def webhook_defn_management(req):
    return
    {
        "messages": [
        {
          "type": 0,
          "platform": "facebook",
          "speech": "defnssss"
        },
        {
          "type": 1,
          "platform": "facebook",
          "title": "GIAC",
          "subtitle": "Defn Management",
          "buttons": [
            {
              "text": "Read more",
              "postback": "https://www.giac.org/certifications/management"
            }
          ]
        },
        {
          "type": 0,
          "speech": ""
        }
      ]

    }

def webhook_giac_management(req):
    
    return {
        "messages": [
        {
          "type": 0,
          "platform": "facebook",
          "speech": "\nBelow is a list of the most popular Management/Audit/Legal certifications that GIAC offer:" \
                    "\n\nGSLC: Security Leadership" \
                    "\nGSNA: Systems and Network Auditor" \
                    "\nGISP: Information Security Professional"
                    "\n\nFor more Management/Audit/Legal certifications visit: https://www.giac.org/certifications/management "
        },
        {
          "type": 1,
          "platform": "facebook",
          "title": "GIAC",
          "subtitle": "Management/Audit certs",
          "buttons": [
            {
              "text": "GSLC more info",
              "postback": ""
            },
            {
              "text": "GSNA more info",
              "postback": ""
            },
            {
              "text": "GISP more info",
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

# webhook for Security Leadership (GSLC)
def webhook_giac_gslc(req):
   
    return {
        "messages": [
        {
          "type": 0,
          "platform": "facebook",
          "speech": "Security Leadership (GSLC) certification gives individuals in depth knowledge on: " \
                    "\n1. Risks of 802.11 wireless networks and how to secure them" \
                    "\n2. Access control and password management" \
                    "\n3. Building a security awareness program" \
                    "\n4. Cryptography applications, VPNs and IPSec." \
                    "\n\nInfo at: https://www.giac.org/certification/security-leadership-gslc" \
                    "\n\nTo obtain GSLC certification, the below training must be completed: "
                    
        },
        {
          "type": 1,
          "platform": "facebook",
          "title": "MGT512",
          "subtitle": "SANS Security Leadership Essentials",
          "buttons": [
            {
              "text": "MGT512 info",
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

# GIAC - SANS Security Leadership Essentials (MGT512)
def webhook_giac_mgt512(req):
    
    return {
        "messages": [
        {
          "type": 0,
          "platform": "facebook",
          "speech": "MGT512: Security Leadership Essentials Training prepares individuals for GSLC certification." \
                    "\n\nThe training course can be completed in 5 days"
        },
        {
          "type": 1,
          "platform": "facebook",
          "title": "More options",
          "buttons": [
            {
              "text": "MGT512 syllabus",
              "postback": ""
            },
            {
              "text": "Laptop",
              "postback": ""
            },
            {
              "text": "Register",
              "postback": "https://www.sans.org/registration/register.php?conferenceid=208"
            }
          ]
        },
        {
          "type": 0,
          "speech": ""
        }
      ]
    }

# webhook for MGT512 syllabus
def webhook_giac_mgt512_syllabus(req):
    
    return {
         "messages": [
        {
          "type": 0,
          "platform": "facebook",
          "speech": "---MGT512 Syllabus---" \
                    "\nDay 1: Managing the Enterprise, Planning, Network, and Physical Plant" \
                    "\nDay 2: IP Concepts, Attacks Against the Enterprise and Defense-in-Depth" \
                    "\nDay 3: Secure Communications" \
                    "\nDay 4: The Value of Information" \
                    "\nDay 5: Management Practicum"
        },
        {
          "type": 1,
          "platform": "facebook",
          "title": "Further info",
          "subtitle": "",
          "buttons": [
            {
              "text": "Laptop",
              "postback": ""
            },
            {
              "text": "Register",
              "postback": "https://www.sans.org/registration/register.php?conferenceid=208"
            },
            {
              "text": "Website",
              "postback": "https://www.sans.org/course/security-leadership-essentials-managers-knowledge-compression#__utma=183869984.18323172.1519689563.1519733474.1519744377.5"
            },
          ]
        },
        {
          "type": 0,
          "speech": ""
        }
      ]
    }

# webhook for Systems and Network Auditor (GSNA)
def webhook_giac_gsna(req):

  
    return {
        "messages": [
        {
          "type": 0,
          "platform": "facebook",
          "speech": "Systems and Network Auditor (GSNA) certification gives individuals in depth knowledge on: " \
                    "\n1. Basic knowledge of risk analysis techniques and be able to conduct a technical audit of essential information systems." \
                    "\n\nInfo at: https: https://www.giac.org/certification/systems-and-network-auditor-gsna" \
                    "\n\nTo obtain GSNA certification, the below training must be completed: " 
        },
        {
          "type": 1,
          "platform": "facebook",
          "title": "AUD507",
          "subtitle": "Auditing & Monitoring Networks, Perimeters & Systems",
          "buttons": [
            {
              "text": "AUD507 info",
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

# AUD507: Auditing & Monitoring Networks, Perimeters & Systems
def webhook_giac_aud507(req):

    return {
         "messages": [
        {
          "type": 0,
          "platform": "facebook",
          "speech": "AUD507: Auditing & Monitoring Networks, Perimeters & Systems Training prepares individuals for GSNA certification." \
                    "\n\nThe training course can be completed in 6 days"
        },
        {
          "type": 1,
          "platform": "facebook",
          "title": "More options",
          "buttons": [
            {
              "text": "AUD507 syllabus",
              "postback": ""
            },
            {
              "text": "Laptop",
              "postback": ""
            },
            {
              "text": "Register",
              "postback": "https://www.sans.org/registration/register.php?conferenceid=208"
            }
          ]
        },
        {
          "type": 0,
          "speech": ""
        }
      ]
    }

# Auditing & Monitoring Networks, Perimeters & Systems (AUD507) syllabus
def webhook_giac_aud507_syllabus(req):

    return {
         "messages": [
        {
          "type": 0,
          "platform": "facebook",
          "speech": "---AUD507 Syllabus---" \
                    "\nDay 1: Effective Auditing, Risk Assessment, Reporting" \
                    "\nDay 2: Effective Network & Perimeter Auditing / Monitoring" \
                    "\nDay 3: Web Application Auditing" \
                    "\nDay 4: Advanced Windows Auditing & Monitoring" \
                    "\nDay 5: Advanced UNIX Auditing & Monitoring" \
                    "\nDay 6: Audit the Flag: A NetWars Experience"
        },
        {
          "type": 1,
          "platform": "facebook",
          "title": "Further info",
          "subtitle": "",
          "buttons": [
            {
              "text": "Laptop",
              "postback": ""
            },
            {
              "text": "Register",
              "postback": "https://www.sans.org/registration/register.php?conferenceid=208"
            },
            {
              "text": "Website",
              "postback": "https://www.sans.org/course/auditing-networks-perimeters-systems#__utma=183869984.1578707992.1516911150.1519227651.1519229972.14"
            },
          ]
        },
        {
          "type": 0,
          "speech": ""
        }
      ]
    }

# webhook for Information Security Professional (GISP)
def webhook_giac_gisp(req):

    return {
        "messages": [
        {
          "type": 0,
          "platform": "facebook",
          "speech": "Information Security Professional (GISP) certification gives individuals in depth knowledge on: " \
                    "\n1. understanding of technical security, information security and system security. " \
                    "\n\nInfo at: https://www.giac.org/certification/information-security-professional-gisp" \
                    "\n\nTo obtain GISP certification, the below training must be completed: " 
        },
        {
          "type": 1,
          "platform": "facebook",
          "title": "MGT414",
          "subtitle": " SANS Training Program for GISP Certification",
          "buttons": [
            {
              "text": "MGT414 info",
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

# GIAC - SANS Training Program for CISSP Certification (MG414)
def webhook_giac_mgt414(req):
   
    return {
        "messages": [
        {
          "type": 0,
          "platform": "facebook",
          "speech": "MGT414: SANS Training Program for CISSP Certification Training prepares individuals for GISP certification." \
                    "\n\nThe training course can be completed in 6 days"
        },
        {
          "type": 1,
          "platform": "facebook",
          "title": "More options",
          "buttons": [
            {
              "text": "MGT414 syllabus",
              "postback": ""
            },
            {
              "text": "Laptop",
              "postback": ""
            },
            {
              "text": "Register",
              "postback": "https://www.sans.org/registration/register.php?conferenceid=208"
            }
          ]
        },
        {
          "type": 0,
          "speech": ""
        }
      ]
    }

def webhook_giac_mgt414_syllabus(req):
    
    return {
        "messages": [
        {
          "type": 0,
          "platform": "facebook",
          "speech": "---MGT414 Syllabus---" \
             "\nDay 1: Security and Risk Management" \
             "\nDay 2: Security Engineering" \
             "\nDay 3: Security Engineering " \
             "\nDay 4: Identity and Access Management" \
             "\nDay 5: Security Assessment and Testing" \
             "\nDay 6: Software Development Security"
        },
        {
          "type": 1,
          "platform": "facebook",
          "title": "Further info",
          "subtitle": "",
          "buttons": [
            {
              "text": "Laptop",
              "postback": ""
            },
            {
              "text": "Register",
              "postback": "https://www.sans.org/registration/register.php?conferenceid=208"
            },
            {
              "text": "Website",
              "postback": "https://www.sans.org/course/sans-plus-s-training-program-cissp-certification-exam#__utma=183869984.18323172.1519689563.1519744377.1520265721.6"
            },
          ]
        },
        {
          "type": 0,
          "speech": ""
        }
      ]
    }

    