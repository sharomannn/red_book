# Stage 1: Build the application
FROM node:lts AS build

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json for dependency installation
COPY package*.json ./

# Install dependencies
RUN npm ci --prefer-offline

# Copy the rest of the application's source code
COPY . .

# Run tests, linting, and build the application
RUN npm run build

# Stage 2: Serve the application using Nginx
FROM nginx:1.21.6

# Set the working directory
WORKDIR /app/dist

# Copy the built application from the build stage
COPY --from=build /app/dist .

# Copy the Nginx configuration file
COPY nginx.conf /etc/nginx/nginx.conf

# Expose port 80
EXPOSE 80

# Start Nginx server
CMD ["nginx", "-g", "daemon off;"]

