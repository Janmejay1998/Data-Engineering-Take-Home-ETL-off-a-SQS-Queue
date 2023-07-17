import hashlib
from typing import Dict, Any
from datetime import datetime


def mask_ip(ip: str) -> str:
    return hashlib.sha256(ip.encode()).hexdigest()


def mask_device_id(device_id: str) -> str:
    return hashlib.sha256(device_id.encode()).hexdigest()


def mask_pii_data(data: Dict[str, Any]) -> Dict[str, Any]:
    masked_data = dict(data)  # Shallow copy of input data
    
    masked_data["masked_ip"] = mask_ip(masked_data["ip"])
    masked_data["masked_device_id"] = mask_device_id(masked_data["device_id"])
    masked_data["create_date"] = datetime.utcnow().date()
    
    return masked_data
