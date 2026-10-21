FROM python:3.13.16-alpine
WORKDIR /usr/local/app

# Copy the "requirements.txt" file into the working directory
COPY requirements.txt ./

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the contents of the "src" directory into the working directory
COPY src ./

# Expose port 5000
EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]
