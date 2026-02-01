import pandas as pd
import re


sector_mapping = {
    'Information Technology': [
        'developer', 'engineer', 'programmer', 'software', 'IT', 'system', 'data scientist',
        'web developer', 'admin', 'support', 'consultant', 'architect', 'technician', 'UX',
        'analyst', 'sysadmin', 'devops', 'infrastructure', 'cloud', 'technical', 'coder',
        'it manager', 'it specialist', 'it consultant', 'it business analyst', 'it auditor',
        'software engineer', 'frontend', 'backend', 'full stack', 'java', 'python'
    ],
    'Education': [
        'teacher', 'instructor', 'professor', 'educator', 'student', 'lecturer', 'principal',
        'tutor', 'trainer', 'educational', 'school', 'language', 'maths', 'science',
        'physical sciences', 'high school', 'bachelor', 'magister', 'phd', 'student advisor'
    ],
    'Healthcare': [
        'psychologist', 'radiographer', 'medical technologist', 'vet', 'nurse', 'therapist',
        'doctor', 'clinical', 'dietitian', 'occupational therapist', 'medical doctor',
        'registered nurse', 'band 5 nurse', 'dentist', 'biopolymer', 'quality control microbiologist'
    ],
    'Administration and support': [
        'admin', 'officer', 'coordinator', 'assistant', 'clerk', 'receptionist', 'support',
        'secretary', 'administrative', 'office manager', 'personal assistant', 'virtual assistant',
        'records manager', 'executive officer', 'administrator', 'asministrative'
    ],
    'Sales and Marketing': [
        'sales', 'account manager', 'marketing', 'retail', 'seller', 'representative',
        'business development', 'key account', 'pricing', 'insurance agent', 'sales rep',
        'senior salesman', 'international sales', 'sales manager', 'marketing director'
    ],
    'Food Service': [
        'cook', 'chef', 'kitchen', 'waitress', 'food', 'barista', 'sushi', 'beverage',
        'restaurant', 'hotel', 'food and beverage', 'main cook', 'line cook'
    ],
    'Engineering and Manufacturing': [
        'engineer', 'mechanic', 'operator', 'technician', 'manufacturing', 'production',
        'machine operator', 'civil engineer', 'structural engineer', 'mining engineer',
        'process engineer', 'quality assurance', 'cnc programmer', 'metallurgical',
        'logistics engineer', 'project engineer', 'food engineer', 'automotive operator'
    ],
    'Law': [
        'lawyer', 'attorney', 'legal', 'paralegal', 'conveyancer', 'legal advisor',
        'counselor', 'jurist', 'advocate', 'barrister'
    ],
    'Academic/Research': [
        'researcher', 'research assistant', 'scientist', 'phd', 'professor', 'lab',
        'laboratory', 'research and development', 'sociologist', 'psychology research'
    ],
    'Arts and Entertainment': [
        'entertainment', 'photo', 'designer', 'graphic designer', 'artist', '3d artist',
        'actress', 'photographer', 'audiovisual', 'sound technician', 'translator'
    ],
    'Public Sector': [
        'police', 'social worker', 'government', 'military', 'soldier', 'firefighter',
        'inspector', 'commissioner', 'security officer', 'protection officer', 'constable'
    ],
    'Finance and Accounting': [
        'accountant', 'controller', 'finance', 'banking', 'payroll', 'financial analyst',
        'accounts officer', 'management accountant', 'finance manager', 'finance coordinator',
        'compliance officer', 'auditor', 'fraud analyst'
    ],
    'Human Resources': [
        'HR', 'human resources', 'recruiter', 'talent', 'workforce', 'hr generalist'
    ],
    'Management and executives': [
        'manager', 'director', 'supervisor', 'lead', 'head', 'chief', 'ceo', 'vp',
        'president', 'executive', 'senior manager', 'general manager', 'branch manager',
        'project manager', 'product manager', 'operations manager', 'development director'
    ],
    'Customer Service': [
        'customer service', 'help desk', 'client', 'customer support', 'call center',
        'customer care', 'service representative', 'front office', 'front desk'
    ],
    'Logistics and Supply Chain': [
        'logistics', 'supply chain', 'warehouse', 'delivery', 'shipping', 'procurement',
        'inventory', 'store', 'retail', 'grocery', 'production coordinator'
    ],
    'Other professional services': [
        'consultant', 'plumber', 'handyman', 'multi tradesman', 'technician', 'fitter',
        'hairdresser', 'butcher', 'farmer', 'janitor', 'waste attendant', 'driver'
    ],
    'Uncategorized': [
        'employed', 'employee', 'full time', 'self employed', 'intern', 'trainee',
        'assistant', 'specialist', 'officer', 'coordinator', 'working', 'staff'
    ]
}


def classify_job(title, mapping):
    if pd.isna(title) or title == '':
        return 'Uncategorized'

    title_lower = title.lower().strip()

    # Special handling of some specific categories
    if any(word in title_lower for word in ['student', 'phd student']):
        return 'Education'

    # Examine management positions (but exclude managers in technical or specialized roles).
    if 'manager' in title_lower or 'director' in title_lower or 'supervisor' in title_lower:
        # If it is a management position in a professional technical field, it should be prioritized for classification under the professional technical category.
        tech_terms = ['it', 'software', 'system', 'technology', 'engineering', 'technical']
        if not any(term in title_lower for term in tech_terms):
            for sector, keywords in mapping.items():
                if sector not in ['Management and senior executives', 'Uncategorized']:
                    for keyword in keywords:
                        if keyword in title_lower and keyword not in ['manager', 'director', 'supervisor']:
                            return sector
            return 'Management and senior executives'

    for sector, keywords in mapping.items():
        for keyword in keywords:
            if re.search(r'\b' + re.escape(keyword) + r'\b', title_lower):
                return sector

    return 'Uncategorized'


# All job data
job_titles = [
     your data
]


sector_counts = {}
classified_jobs = []

for job in job_titles:
    sector = classify_job(job, sector_mapping)
    classified_jobs.append((job, sector))
    sector_counts[sector] = sector_counts.get(sector, 0) + 1

df = pd.DataFrame(classified_jobs, columns=['Job Title', 'Sector'])


print("=" * 50)
print("Employment sector distribution statistics:")
print("=" * 50)

total_jobs = len(job_titles)
for sector, count in sorted(sector_counts.items(), key=lambda x: x[1], reverse=True):
    percentage = (count / total_jobs) * 100
    print(f"{sector}: {count}人 ({percentage:.1f}%)")

print(f"\ntotal_jobs: {total_jobs}")
print("=" * 50)

# Display detailed job listings for each department
print("\nDetailed classification results (showing the first 5 jobs for each department as an example):")
for sector in sorted(sector_counts.keys()):
    sector_jobs = [job for job, sec in classified_jobs if sec == sector]
    print(f"\n{sector} ({len(sector_jobs)}jobs):")
    for job in sector_jobs[:5]:
        print(f"  - {job}")
    if len(sector_jobs) > 5:
        print(f"  ...There are {len(sector_jobs) - 5} jobs left")
