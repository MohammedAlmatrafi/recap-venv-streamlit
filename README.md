## Streamlit application with virtual environment

This is an example Streamlit application set up with a conda virtual environment created for educational purposes.

### Steps to make a Streamlit application w/venv

1- Run `git init` in empty project folder to set up git for deployment later.

2- Run `conda create --name <ENV_NAME> python=<PY_VERSION>` to create a virtual environment for easily sharing the used packages. Note: replace ENV_NAME with desired environment name e.g. `myenv`. Also replace PY_VERSION with the desired Python version e.g. `3.10`

3- Run `conda activate <ENV_NAME>` to activate the virtual environment you just created. This allows you to install the packages inside this package.

4- Create a Python file with any name you desire e.g. `app.py`

5- Install Streamlit package via `pip install streamlit`

6- Install any additional packages you need e.g. `pip install langchain openai`

7- \*Optional step\* Create `.env` file that contain project secrects like `OPENAI_API_KEY` to your project folder

8- \*IMPORTANT\* If you have created a `.env` file, make sure you also create a `.gitignore` file and write down all files you wish to ignore including `.env`

9- Create a Streamlit app by following the official documentation at [Streamlit docs](https://docs.streamlit.io/get-started/fundamentals/main-concepts)

10- Save the current state of your virtual environment using `conda env export > environment.yml`. This will create an `environment.yml` file that lists all the dependencies of your project.

11- To run your Streamlit application, use the command `streamlit run app.py` (replace `app.py` with the name of your Python file if different).

12- If you want to share your project, push your code to a Git repository and include the `environment.yml` file so others can recreate the same environment using `conda env create -f environment.yml --name <ENV_NAME>`.

13- For deployment, refer to the [Streamlit deployment guide](https://docs.streamlit.io/streamlit-community-cloud) or other hosting platforms like Heroku or AWS.

That's it!
