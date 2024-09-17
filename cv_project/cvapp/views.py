
from django.shortcuts import render

def cv_view(request):
    context = {
        'name': 'Shreya Srinivasan Bharadwaj',
        'phone': '+19297544166',
        'email': 'ss19652@nyu.edu',
        'linkedin': 'https://www.linkedin.com/in/shreya-srinivasan-bharadwaj-b78b23203',
        'linkedin_name': 'Shreya Srinivasan Bharadwaj',
        'education': [
            {
                'name': 'New York University',
                'degree': "Master's in Computer Science",
                'dates': '2024 -- 2026',
                'location': 'Brooklyn, New York'
            },
            {
                'name': 'Visvesvaraya Technological University',
                'degree': 'Bachelor of Engineering in Computer Science (CGPA: 9.37)',
                'dates': 'Dec. 2020 -- May 2024',
                'location': 'Shivamogga, India'
            }
        ],
        'experience': [
            {
                'company': 'Ekathva Innovations Pvt Ltd',
                'title': 'Backend AI Developer Intern',
                'dates': 'Aug. 2023 -- Sept. 2023',
                'location': 'Shivamogga, Karnataka',
                'responsibilities': [
                    'Worked with key AI topics including PyTorch, NumPy, NLP, MLP, BERT models, and RNN.',
                    'Explored these topics with hands-on experience in Google Colab environment and developed a basic text generator.',
                    'Designed a grammar checker using BERT for comprehensive understanding of Deep Learning using PyTorch.'
                ]
            },
            {
                'company': 'ANS Charitable Trust',
                'title': 'Content Creator Intern',
                'dates': 'May 2022 -- July 2022',
                'location': 'Remote',
                'responsibilities': [
                    'Crafted promotional content and collaborated with the design team to curate content for social media.',
                    'Composed emails describing the Fit Fest for former and prospective clientele.',
                    'Exhibited problem-solving skills by generating effective marketing ideas to advertise the campaign.'
                ]
            }
        ],
        'projects': [
            {
                'name': 'Hotel Management System',
                'technologies': 'Java, MySQL',
                'date': 'December 2022',
                'details': [
                    'Developed a robust Hotel Management System utilizing Java Swing for an intuitive front-end interface.',
                    'Designed a well-structured database schema and used MySQL queries for transaction management.'
                ]
            },
            {
                'name': 'E-commerce App',
                'technologies': 'Kotlin, Android Studio',
                'date': 'May 2023',
                'details': [
                    'Created an Android application using Kotlin and Android Studio for both seller and consumer services.',
                    'Worked with Google Firebase to manage user data across multiple platforms.'
                ]
            },
            {
                'name': 'Grammar Checker',
                'technologies': 'Python, NLP, BERT',
                'date': 'September 2023',
                'details': [
                    'Utilized BERT to build a grammar checking system that evaluates grammatical correctness of English sentences.',
                    'Trained the model using PyTorch on the CoLA dataset for accurate error detection.'
                ]
            }
        ],
        'skills': {
            'languages': 'Java, Python, C, HTML/CSS, JavaScript, SQL',
            'developer_tools': 'VS Code, Eclipse, Android Studio',
            'software_tools': 'Figma, Canva, WordPress, MS Office'
        },
        'achievements': [
            'Secured an elite gold certificate in NPTEL exam on DSA using Java by IIT in 2023.',
            'Honored as 1 among the 23 NIAS-MAIYA Prodigy Fellows of 2019.',
            'Won 1st prize in an intercollegiate UI design competition in 2022.',
            'Co-authored 10+ poetry anthologies in 2022.',
            'Active Blogger on WordPress blog site since 2021.',
            'Served as the Rotary Interact Club President in class 10.'
        ]
    }
    
    return render(request, 'cvapp/cv.html', context)

