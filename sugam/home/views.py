from django.http import JsonResponse
from .models import DocSummarized
from .GenerateFollowup import GenerateFollowup
from .VoiceToText import VoiceToText
from .ImageToText import ImageToText
from .Summarizer import Summarizer

def upload(request):
    if request.method == 'POST':
        # Assuming the image is sent as a file in the 'image' field
        uploaded_image = request.FILES.get('image')
        user_lang      = request.POST["lang"]

        # Process the image and extract the text
        img_to_txt =  ImageToText(uploaded_image)
        extracted_txt = img_to_txt.start()

        summarize =  Summarizer(extracted_txt, user_lang)
        summarized_txt = summarize.start()

        doc_sum = DocSummarized(original_txt=extracted_txt, summarized_txt=summarized_txt)
        doc_sum.save()

        # Create the JSON response
        response_data = {
            'text': summarized_txt,
            'id': doc_sum.id,
        }

        return JsonResponse(response_data)

    # Handle other HTTP methods (e.g., GET) if needed
    return JsonResponse({'error': 'Invalid request method'}, status=405)

def follow_up(request):
    if request.method == 'POST':
        doc_id = request.GET.get('id')
        # Assuming the voice file is sent as a file in the 'voice' field
        uploaded_voice = request.FILES.get('voice')

        doc = DocSummarized.objects.get(id=doc_id)
        original_text = doc.original_txt
        summarized_text = doc.summarized_txt

        # Process the voice and extract the question text
        voice_to_text =  VoiceToText(uploaded_voice)
        extracted_question = voice_to_text.start()

        gen_follow_up = GenerateFollowup(original_text, summarized_text)
        follow_up = gen_follow_up.start(extracted_question)

        # Create the JSON response
        response_data = {
            'question': extracted_question,
            'followup': follow_up,  
        }

        return JsonResponse(response_data)

    # Handle other HTTP methods (e.g., PUT, DELETE) if needed
    return JsonResponse({'error': 'Invalid request method'}, status=405)
