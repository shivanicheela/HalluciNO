"""
Quick start script for HalluciNO development

This script helps set up and run both frontend and backend automatically
"""

import os
import sys
import subprocess
import platform

def run_command(cmd, shell=False):
    """Execute a command and return success status"""
    try:
        subprocess.run(cmd, shell=shell, check=True)
        return True
    except subprocess.CalledProcessError:
        return False

def setup_backend():
    """Setup and run backend"""
    print("\n" + "="*50)
    print("🔧 Setting up Backend...")
    print("="*50)
    
    os.chdir("backend")
    
    # Check Python
    if not run_command(["python", "--version"]):
        print("❌ Python not found! Install Python 3.8+")
        return False
    
    # Create virtual environment
    print("📦 Creating virtual environment...")
    if platform.system() == "Windows":
        run_command(["python", "-m", "venv", "venv"])
        activate_cmd = "venv\\Scripts\\activate.bat && "
    else:
        run_command(["python3", "-m", "venv", "venv"])
        activate_cmd = "source venv/bin/activate && "
    
    # Install dependencies
    print("📥 Installing dependencies...")
    if platform.system() == "Windows":
        run_command("venv\\Scripts\\pip install -r requirements.txt", shell=True)
    else:
        run_command(". venv/bin/activate && pip install -r requirements.txt", shell=True)
    
    print("✅ Backend setup complete!")
    os.chdir("..")
    return True

def setup_frontend():
    """Setup frontend"""
    print("\n" + "="*50)
    print("🎨 Setting up Frontend...")
    print("="*50)
    
    os.chdir("frontend")
    
    # Check Node
    if not run_command(["node", "--version"]):
        print("❌ Node.js not found! Install Node.js 18+")
        return False
    
    # Install dependencies
    print("📥 Installing dependencies...")
    if not run_command(["npm", "install"]):
        print("❌ Failed to install frontend dependencies")
        return False
    
    print("✅ Frontend setup complete!")
    os.chdir("..")
    return True

def main():
    print("""
    ╔═══════════════════════════════════════════════════════╗
    ║     🤖 HalluciNO - AI Hallucination Detector 🎮      ║
    ║                  Quick Start Setup                    ║
    ╚═══════════════════════════════════════════════════════╝
    """)
    
    if len(sys.argv) > 1 and sys.argv[1] == "--help":
        print("""
        Usage: python quickstart.py [option]
        
        Options:
        --help          Show this help message
        --backend-only  Setup only backend
        --frontend-only Setup only frontend
        (no option)     Setup both backend and frontend
        """)
        return
    
    backend_only = "--backend-only" in sys.argv
    frontend_only = "--frontend-only" in sys.argv
    
    # Get to project root
    if os.path.exists("backend") and os.path.exists("frontend"):
        root_dir = os.getcwd()
    else:
        print("❌ Error: Run this script from the HalluciNO project root!")
        return
    
    try:
        # Setup backend
        if not frontend_only:
            if not setup_backend():
                print("⚠️  Backend setup had issues. Continuing...")
        
        # Setup frontend
        if not backend_only:
            if not setup_frontend():
                print("⚠️  Frontend setup had issues.")
                return
        
        # Print next steps
        print("""
        ╔═══════════════════════════════════════════════════════╗
        ║                  ✅ Setup Complete!                   ║
        ╚═══════════════════════════════════════════════════════╝
        
        🚀 Next Steps:
        
        1. Start Backend (in one terminal):
           cd backend
        """ + ("  venv\\Scripts\\activate" if platform.system() == "Windows" else "  source venv/bin/activate") + """
           python run.py
        
        2. Start Frontend (in another terminal):
           cd frontend
           npm start
        
        3. Open http://localhost:4200 in your browser
        
        📚 Documentation:
        - Setup Guide: See SETUP.md
        - Deployment: See DEPLOY.md
        - API Docs: http://localhost:8000/docs
        
        🎮 Have fun playing HalluciNO!
        """)
        
    except Exception as e:
        print(f"❌ Error during setup: {e}")

if __name__ == "__main__":
    main()
