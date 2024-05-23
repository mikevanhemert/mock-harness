import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from schemas import *

#config = yaml.safe_load(open("config/config.yml"))

formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
if logger.handlers:
    # we assume the first handler is the one we want to configure
    console = logger.handlers[0]
else:
    console = logging.StreamHandler()
    logger.addHandler(console)
console.setFormatter(formatter)
console.setLevel(logging.DEBUG)

app = FastAPI()

# disable CORS for now
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

config = PlatformConfig(platform='eks', prefix="mockDeploy")

@app.get("/")
async def root():
    logger.debug("root endpoint called")
    return {"message": "Hello World"}

@app.get("/configure")
async def get_config():
    logger.debug("config endpoint called")
    return config

@app.post("/configure")
async def set_config(payload: PlatformConfig):
    logger.debug("configure endpoint called with %s", payload)
    global config
    config = payload
    return config

@app.post("/deployPlatform")
async def set_config(payload: DeployPlatform):
    logger.debug("configure endpoint called with %s", payload)
    return payload

@app.post("/deployContent")
async def set_config(payload: DeployContent):
    logger.debug("configure endpoint called with %s", payload)
    return payload
