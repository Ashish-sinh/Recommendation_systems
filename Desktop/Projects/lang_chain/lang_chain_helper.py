import os 
from secrate_key import openapi_key 
from langchain import OpenAI 
from langchain.prompts import PromptTemplate 
from langchain.chains import LLMChain 
from langchain.chains import SequentialChain 
os.environ['OPENAI_API_KEY']  = openapi_key 

my_llm = OpenAI(temperature = 0.7) 


def name_and_menu_generator(cuisine)  : 

    # Resturant Name : 

    prompt_template_name = PromptTemplate ( 
        input_variables = ['cuisine'] , 
        template = "I  want to open Resturant for the {cuisine}.Suggest Fancy Name for this"
    )

    name_chain = LLMChain(llm = my_llm , prompt = prompt_template_name , output_key = 'Resturant_Name') 

    # menu items : 

    prompt_template_items = PromptTemplate ( 
        input_variables  = ['Resturant_Name'] , 
        template = 'Pleease Provide the Menu Items according to my {Resturant_Name}.return it as coma saprated string' 
    ) 

    menu_chain = LLMChain( llm = my_llm , prompt= prompt_template_items , output_key = 'menu_items' )

    chain = SequentialChain( 
        chains = [name_chain , menu_chain ] , 
        input_variables = ['cuisine'] , 
        output_variables = ['Resturant_Name','menu_items'] 
    )


    responce = chain({'cuisine':cuisine })


    return responce 


if __name__ == "__main__" : 
    print(name_and_menu_generator('Gujrati'))