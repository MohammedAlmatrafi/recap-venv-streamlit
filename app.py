import streamlit as st
from langchain.agents import Tool, initialize_agent, AgentType
from langchain.chat_models import ChatOpenAI
import requests
import os
import dotenv

dotenv.load_dotenv()


# Function to get weather data
def get_weather(address: str) -> str:
    """
    Fetches real-time weather info using a weather API based on the input address.
    """
    weather_api_key = os.getenv(
        "WEATHER_API_KEY"
    )  # Ensure you have set this in your environment variables
    base_url = (
        f"https://api.weatherapi.com/v1/current.json?key={weather_api_key}&q={address}"
    )

    try:
        response = requests.get(base_url)
        response.raise_for_status()
        data = response.json()

        # Extract weather details
        temp = data["current"]["temp_c"]
        description = data["current"]["condition"]["text"]

        return f"The current weather in {address} is {temp}°C, {description}."
    except requests.exceptions.RequestException as e:
        return f"Error fetching weather data: {e}"
    except KeyError as e:
        return f"Could not retrieve weather information. Please check the address name or try again later. {e}"


# Weather tool
weather_tool = Tool(
    name="weather_api",
    func=get_weather,
    description="Useful for when you need to know the current weather in a city. Input should be the city name.",
)

# Setup LangChain LLM and agent with tools
llm = ChatOpenAI(temperature=0, model="gpt-4o-mini")

tools = [weather_tool]

agent = initialize_agent(
    tools=tools, llm=llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)

# Streamlit UI
st.title("🧠 AI Agent with Weather Tool")

user_input = st.text_input("Enter city:")

if user_input:
    with st.spinner("Thinking..."):
        response = agent.run(user_input)
    st.write("### 🤖 Response:")
    st.write(response)
