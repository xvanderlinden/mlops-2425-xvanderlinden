# Use Node.js Alpine image for a smaller footprint
FROM node:20-alpine

# Create app directory
WORKDIR /app

# Copy only the package.json and yarn.lock to install dependencies
COPY package.json yarn.lock ./

# Install dependencies
RUN yarn install --frozen-lockfile

# Copy the rest of the application code
COPY . .

# Expose port 3000
EXPOSE 3000

# Start the application
CMD ["yarn", "start"]


# Explanation:

#   Base Image: We use the lightweight Alpine version of Node.js 20.x.x to keep the image small.
#   Working Directory: The WORKDIR sets the default directory inside the container to /app.
#   Copy Dependencies: Copy package.json and yarn.lock to install dependencies separately before copying the app code.
#   Install Dependencies: yarn install --frozen-lockfile ensures the dependencies are installed exactly as specified in the lockfile.
#   Copy the App: The COPY . . command copies the app's source code to the container.
#   Expose Port: The container exposes port 3000 to the host.
#   Start the App: CMD ["yarn", "start"] tells Docker to run the app when the container starts.