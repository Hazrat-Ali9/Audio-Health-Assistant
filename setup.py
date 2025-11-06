from setuptools import setup, find_packages

setup(
    name='ai_audio_health_assistant',
    version='0.1.0',
    description='An AI Audio Health Assistant using Speech Recognition and GPT-4',
    author='rhs lion34',
    author_email='your_email@example.com',  # Replace with your email
    packages=find_packages(),
    install_requires=[
        'speechrecognition',
        'gtts',
        'streamlit',
        'openai',
        'numpy',
        'pydub',
        'langdetect',
        'sounddevice',
        'soundfile'
    ],
    entry_points={
        'console_scripts': [
            'run-assistant=app:main',  # Ensure there's a main function in your app.py if you want to use this.
        ],
    },
)
