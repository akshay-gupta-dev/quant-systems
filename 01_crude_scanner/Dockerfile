# 1. Base Image: Use a lightweight Python version
FROM python:3.10-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Install system dependencies (needed for TA-Lib if we add it later)
RUN apt-get update && apt-get install -y gcc

# 4. Install Python libraries
# We list them directly to keep it simple for now
RUN pip install pandas yfinance matplotlib

# 5. Copy your script into the container
COPY crude_bot.py .

# 6. Command to run when container starts
CMD ["python", "crude_bot.py"]