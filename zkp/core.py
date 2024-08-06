# zkp/core.py

from .zkp import ConcreteZKP
from typing import Any, Dict

# example to use the ConcreteZKP class
def create_and_verify_proof(computation: Any, 
                            data: Any) -> Dict[str, Any]:
    zkp_instance = ConcreteZKP(name="Example ZKP")
    result = zkp_instance(computation, data)
    return result
