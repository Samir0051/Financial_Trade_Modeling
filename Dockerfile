# 1. Use an official, lightweight Python image
FROM python:3.9-slim

# 2. Set a working directory inside the container
WORKDIR /app

# 3. Copy only requirements first (to leverage Docker layer caching)
COPY requirements.txt .

# 4. Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of the application code
COPY modeling.py .

# 6. (Optional) If you have more scripts or modules, copy them too:
# COPY some_module.py . 
# COPY other_folder/ other_folder/

CMD ["python", "modeling.py"]