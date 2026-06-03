# # Use a lightweight Windows base image
# FROM mcr.microsoft.com/windows/nanoserver:1809

# # Set the working directory inside the container
# WORKDIR /SpaceProjectTm1_Quiz

# # Copy your batch script from the host to the container
# COPY run.bat .

# # Define the entrypoint to execute the batch file when the container starts
# # Uses cmd.exe /c to run the script and terminate
# ENTRYPOINT ["cmd.exe", "/c", "run.bat"]   