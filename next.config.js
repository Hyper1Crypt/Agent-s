/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  env: {
    NEXT_PUBLIC_API_URL: process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000',
  },
  eslint: {
    ignoreDuringBuilds: true,
  },
  // Disabilita anche il linting durante il build
  typescript: {
    ignoreBuildErrors: true,
  },
  typescript: {
    // Opzionale: disabilita anche TypeScript check durante build se necessario
    ignoreBuildErrors: false,
  },
}

module.exports = nextConfig

