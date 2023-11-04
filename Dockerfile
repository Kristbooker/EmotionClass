# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

COPY ./app /app/app
COPY ./model /app/model
# Copy the current directory contents into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt




EXPOSE 5000

# Define environment variable for model path
ENV MODEL_PATH=/model/TextModel.pkl


# Run app.py when the container launches
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]
