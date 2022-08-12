import re #rejects
import l_responses as long

#function that calculates the probability that the message is the corresponding message
def message_probability(user_message,recognised_words,single_response=False,required_words=[]):
    message_certainty=0
    has_required_words=True

      #Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty+=1

#Calculates the percent of recognised words in a user message
    percentage=float(message_certainty) / float(len(recognised_words))

    for word in required_words:
        if word not in user_message:
            has_required_words=False
            break
    
    if has_required_words or single_response:
        return int(percentage*100)
    else:
        return 0

def check_all_messages(message):
    highest_prob_list={}

    def response(bot_response,list_of_words,single_response=False,required_words=[]):
         nonlocal highest_prob_list
         highest_prob_list[bot_response] =message_probability(message,list_of_words,single_response,required_words)

#Responses-----------------------------------------------------------------

    response('Hello!',['hello','hi','sup','hey','heyo'],single_response=True)
    response('I am doing fine,and you?',['how','are','you','doing'],required_words=['how'])
    response('That sounds great!',['i','am','fine','good','okay','well','not so good'],required_words=['i','am','fine','good','okay','well','not so good'])
    response('Thank you!',['you','are','good','awesome','best','great','amazing','nice'],required_words=['you','good','awesome','best','great','amazing','nice'])
    response(long.r_eating,['what','you','eat'],required_words=['you','eat'])

    best_match=max(highest_prob_list,key=highest_prob_list.get)
    #print(highest_prob_list)

    return long.unknown() if highest_prob_list[best_match]<1 else best_match


def get_response(user_input):
    #removing all symbols so as to read the words separately
    split_message=re.split(r'\s+|[,;?!.-]\s*',user_input.lower())
    response=check_all_messages(split_message)
    return response



#Testing the response system

while True: #Infinite While true loop so that we always get responses
   print("Bot: "+get_response(input("You:  ")))