import streamlit as st
import boto3
import json 
import re

#The Bedrock region
region = "us-west-2"


def parse_xml_reviews(xml_data):
    positives = re.findall(r'<Positives>(.*?)</Positives>', xml_data, re.DOTALL)
    neutrals = re.findall(r'<Neutrals>(.*?)</Neutrals>', xml_data, re.DOTALL)
    negatives = re.findall(r'<Negatives>(.*?)</Negatives>', xml_data, re.DOTALL)

    # Extract individual elements from the captured groups
    positive_elements = re.findall(r'<Element>(.*?)</Element>', positives[0]) if positives else []
    neutral_elements = re.findall(r'<Element>(.*?)</Element>', neutrals[0]) if neutrals else []
    negative_elements = re.findall(r'<Element>(.*?)</Element>', negatives[0]) if negatives else []

    return positive_elements, neutral_elements, negative_elements

def parse_review(review):
    bedrock = boto3.client(service_name='bedrock-runtime', region_name=region)
    
    modelId = 'anthropic.claude-v2'
    accept = 'application/json'
    contentType = 'application/json'
    prompt = "\n\nHuman: You are a shopping assistant designed by Amazon. You are reading reviews and provide a list of the positive, neutral and negative aspects of the product. The goal is to help customers decide if they want to buy it or not. Each element of the list should be maximum 3 words. You must answer using this XML format. <Positives><Element>XXX</Element><Neutrals>... <Negatives>...  Always write  the elements in English\n\nAssistant: Understood"
    prompt += "\n\nHuman: Amazon Review: "+review+"\n\nAssistant:"
    body = json.dumps({
            "prompt": prompt,
            "max_tokens_to_sample": 8000,
            "temperature": 0.1,
            "top_p": 1,
        })
    response = bedrock.invoke_model(body=body, modelId=modelId, accept=accept, contentType=contentType)
    response_body = json.loads(response.get('body').read())
    return parse_xml_reviews(response_body.get("completion"))

def main():
    st.title("Amazon Review Analyzer")

    # Text area for input
    review_text = st.text_area("Paste an Amazon Review:", height=150)
    
    # Submit button
    if st.button("Analyze Review"):
        if review_text:
            # Call your parse_review function
            positive,neutral,negative = parse_review(review_text)
            col1, col2, col3 = st.columns(3)

            # Displaying the positives in the first column
            with col1:
                st.subheader("Positives:")
                for item in positive:
                    st.success(item)

            # Displaying the neutrals in the second column
            with col2:
                st.subheader("Neutrals:")
                for item in neutral:
                    st.warning(item)

            # Displaying the negatives in the third column
            with col3:
                st.subheader("Negatives:")
                for item in negative:
                    st.error(item)
        else:
            st.error("Please paste a review to analyze.")

if __name__ == "__main__":
    main()