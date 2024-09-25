# Use an official Python runtime as a parent image
FROM python

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make sure we have the OpenAI key as an environment variable
ENV OPENAI_API_KEY="your_openai_api_key_here"

# Run app.py when the container launches
CMD ["python", "app.py"]

