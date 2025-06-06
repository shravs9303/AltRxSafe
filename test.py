import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'altrxsafe.settings')
django.setup()

# Now import the service
from drug_assistant.services.biobert_service import BioBERTService

if __name__ == "__main__":
    service = BioBERTService.get_instance()

    question = "What are the side effects of ibuprofen?"
    drug = "ibuprofen"
    context = service.get_drug_information(drug)

    result = service.answer_question(question, context)
    
    print("Answer:", result["answer"])
    print("Confidence:", result["confidence"])
