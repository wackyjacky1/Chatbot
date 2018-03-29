#----------------------------------------------------- GIAC cyber defense courses ---------------------------------------------------
def webhook_defn_cd(req):

  return{
      "messages": [
        {
          "type": 0,
          "platform": "facebook",
          "speech": "Proactive cyber defense or active cyber defense (ACD) means acting " \
                    "in anticipation to oppose an attack involving computers and networks." \
                    " Proactive cyber defense will most often require additional cybersecurity " \
                    "from internet service providers - wikipedia "
        },
        {
          "type": 1,
          "platform": "facebook",
          "title": "Techopedia",
          "subtitle": "Defn Cyber Defense",
          "buttons": [
            {
              "text": "Read more",
              "postback": "https://www.techopedia.com/definition/6705/cyber-defense"
            }
          ]
        },
        {
          "type": 0,
          "speech": ""
        }
      ]
  }

def webhook_giac_cyber_defense(req):
   
    return {
        "messages": [
        {
          "type": 0,
          "platform": "facebook",
          "speech": "\nBelow is a list of the most popular Cyber Defense certifications that GIAC offer:" \
                    "\nGSEC - Security Essentials" \
                    "\nGCIA - Certified Intrusion Analyst" \
                    "\nGISF - Information Security Fundamentals"
                    "\n\nFor more Cyber Defense certifications visit: https://www.giac.org/certifications/cyber-defense "
        },
        {
          "type": 1,
          "platform": "facebook",
          "title": "GIAC",
          "subtitle": "Cyber Defense Certs",
          "buttons": [
            {
              "text": "GSEC more info",
              "postback": ""
            },
            {
              "text": "GCIA more info",
              "postback": ""
            },
            {
              "text": "GISF more info",
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

# webhook for GSEC Security Essentials certification
def webhook_giac_gsec(req):
  
    return {
        "messages": [
        {
          "type": 0,
          "platform": "facebook",
          "speech": "\nSecurity Essentials (GSEC) certification gives individuals an in depth knowledge on: " \
                    "\n\n1. Preventing attacks and detect network adversaries" \
                    "\n2. Networks, Defense and Secure communications"\
                    "\n3. Foundational linux skills" \
                    "\n\nMore info at: https://www.giac.org/certification/security-essentials-gsec" \
                    "\n\nHowever in order to obtain Security Essentials (GSEC) certification one must complete appropriate training: " \
                    
        },
        {
          "type": 1,
          "platform": "facebook",
          "title": "SEC401",
          "subtitle": "Security Essentials Bootcamp Style Training",
          "buttons": [
            {
              "text": "SEC401 info",
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

# webhook for SEC401 Security Essentials Bootcamp Style Training
def webhook_giac_sec401(req):

    return {
        "messages": [
        {
          "type": 0,
          "platform": "facebook",
          "speech": "SEC401 Security Essentials Bootcamp Style Training prepares individuals for the GSEC certification." \
                    "\n\nThe training course can be completed in 6 days"
        },
        {
          "type": 1,
          "platform": "facebook",
          "title": "More options",
          "buttons": [
            {
              "text": "SEC401 syllabus",
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

# webhook for SEC401 syllabus
def webhook_giac_sec401_syllabus(req):

    return {
        "messages": [
        {
          "type": 0,
          "platform": "facebook",
          "speech": "---SEC401 Syllabus---" \
                    "\nDay 1: Network Security Essentials" \
                    "\nDay 2: Defense-In-Depth and Attacks" \
                    "\nDay 3: Threat Management" \
                    "\nDay 4: Cryptography, Risk Management and Response" \
                    "\nDay 5: Windows Security" \
                    "\nDay 6: Linux Security" 
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
              "postback": "https://www.sans.org/course/security-essentials-bootcamp-style#__utma=183869984.18323172.1519689563.1521638962.1521640052.20"
            },
          ]
        },
        {
          "type": 0,
          "speech": ""
        }
      ]
    }

# Laptop requirements for any GIAC certification
def webhook_giac_laptop(req):
    
    return {
        "messages": [
        {
          "type": 0,
          "platform": "facebook",
          "speech": " Laptop Reuirements:" \
             "\n1. Windows 64-bit version" \
             "\n2. 8 GB RAM" \
             "\n3. 50 GB of available disk space" \
             "\n4. Administrator access and no personal data" \
             "\n5. USB port" \
             "\n6. Download and install VMware Workstation 11, VMware Fusion 7, or VMware Player 7 or higher versions on your system prior to class beginning"
        },
        {
          "type": 1,
          "platform": "facebook",
          "title": "Further info",
          "buttons": [
            {
              "text":" Register",
              "postback": "https://www.sans.org/registration/register.php?conferenceid=208"
            },
            {
              "text":"Website",
              "postback": "https://www.giac.org/certifications"
            }
          ]
        },
        {
          "type": 0,
          "speech": ""
        }
      ]
    }


# webhook for Certified Intrusion Analyst  (GCIA)
def webhook_giac_gcia(req):
    
    print(speech)
    return {
         "messages": [
        {
          "type": 0,
          "platform": "facebook",
          "speech": "Certified Intrusion Analyst  (GCIA) certification gives individuals an in depth knowledge on: \n1. Understanding fundamentals of Traffic Analysis\n2. Understanding open source IDS: Snort and Bro\n3. Network Traffic Forensics and Monitoring\n\nInfo at:  https://www.giac.org/certification/certified-intrusion-analyst-gcia\n\nHowever in order to obtain Intrusion Analyst  (GCIA) certification one must complete appropriate training: "
        },
        {
          "type": 1,
          "platform": "facebook",
          "title": "SEC503",
          "subtitle": "Intrusion Detection In-Depth Training",
          "buttons": [
            {
              "text": "SEC503 info",
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

# webhook for SEC503 Intrusion Detection In-Depth Training
def webhook_giac_sec503(req):
  
    return {
         "messages": [
        {
          "type": 0,
          "platform": "facebook",
          "speech": "SEC503 Intrusion Detection In-Depth Training Training prepares individuals for the GCIA certification." \
                    "\n\nThe training course can be completed in 6 days"
        },
        {
          "type": 1,
          "platform": "facebook",
          "title": "More options",
          "buttons": [
            {
              "text": "SEC503 syllabus",
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

# webhook for SEC503 syllabus
def webhook_giac_sec503_syllabus(req):

    return {
        "messages": [
        {
          "type": 0,
          "platform": "facebook",
          "speech": "---SEC503 Syllabus---" \
                    "\nDay 1: Fundamentals of Traffic Analysis" \
                    "\nDay 2: Fundamentals of Traffic Analysis" \
                    "\nDay 3: Application Protocols and Traffic Analysis" \
                    "\nDay 4: Network Monitoring" \
                    "\nDay 5: Network Traffic Forensics" \
                    "\nDay 6: NetWars: IDS Version" 
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
              "postback": "https://www.sans.org/course/intrusion-detection-in-depth#__utma=183869984.18323172.1519689563.1521640052.1521645460.21&__utmb=183869984.3.9.1521646630863&__utmc=183869984&__utmx=-&__utmz=183869984.1521645460.21.5.utmcsr=l.facebook.com|utmccn=(referral)|utmcmd=referral|utmcct=/&__utmv=-&__utmk=162452156"
            },
          ]
        },
        {
          "type": 0,
          "speech": ""
        }
      ]
    }

# webhook for Information Security Fundamentals (GISF)
def webhook_giac_gisf(req):

    return {
        "messages": [
        {
          "type": 0,
          "platform": "facebook",
          "speech": "Information Security Fundamentals (GISF) certification gives individuals in depth knowledge on: \n1. Information Security Foundations\n2. Cryptography\n3. Network Protection Strategies and Host Protection\n\nInfo at:  https://www.giac.org/certification/information-security-fundamentals-gisf\n\nHowever in order to obtain Information Security Fundamentals (GISF) certification one must complete appropriate training:"
        },
        {
          "type": 1,
          "platform": "facebook",
          "title": "SEC301",
          "subtitle": "Intro to Information Security",
          "buttons": [
            {
              "text": "SEC301 more info",
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

# webhook for SEC301 Intro to Information Security Training
def webhook_giac_sec301(req):

    return {
        "messages": [
        {
          "type": 0,
          "platform": "facebook",
          "speech": "SEC301 Intro to Information Security Training prepares individuals for GISF certification." \
                    "\n\nThe training course can be completed in 5 days."
        },
        {
          "type": 1,
          "platform": "facebook",
          "title": "More options",
          "buttons": [
            {
              "text": "SEC301 syllabus",
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

# webhook for SEC301 syllabus
def webhook_giac_sec301_syllabus(req):

    return {
        "messages": [
        {
          "type": 0,
          "platform": "facebook",
          "speech": "---SEC301 Syllabus---" \
                    "\nDay 1: Security's Foundation" \
                    "\nDay 2: Computer Functions and Networking" \
                    "\nDay 3: An Introduction to Cryptography" \
                    "\nDay 4: Cyber Security Technologies Part 1" \
                    "\nDay 5: Cyber Security Technologies Part 2" \
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
              "postback": "https://www.sans.org/course/intro-information-security#__utma=183869984.1578707992.1516911150.1519472780.1519489927.24"
            },
          ]
        },
        {
          "type": 0,
          "speech": ""
        }
      ]
    }

