from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from fastapi import FastAPI, Response
import uvicorn
from typing import Any

# App creation
app = FastAPI(title="Calculatrice Monitorée")

# Metrics creation: Total number of operation
calc_counter = Counter('calc_ops_total',
                       'Nombre total d\'opération de calcul',
                       ['operation_type'])

# Addition function: A+B
@app.get("/add")
async def add(a: float, b: float) -> dict[str, Any]:
    """
    Do an addition of a and b
    
    :param a: Float number
    :type a: float
    :param b: Float number
    :type b: float
    :return: Un dictionnaire contenant les opérandes, le nom de l'action et le résultat
    :rtype: dict[str, float]
    """

    calc_counter.labels(operation_type="addition").inc()
    result = {"operation":"addition",
                "a":a,
                "b":b, 
                'result':a+b 
            }
    return result

# Substraction function: A-B
@app.get("/sub")
async def sub(a: float, b: float) -> dict[str, Any]:
    """
    Substract B from A
    
    :param a: Float number 
    :type a: float
    :param b: Float number
    :type b: float
    :return: Un dictionnaire contenant les opérandes, le nom de l'action et le résultat
    :rtype: dict[str, float]
    """

    calc_counter.labels(operation_type="substraction").inc()
    result = {"operation":"substraction",
                "a":a,
                "b":b, 
                'result':a-b 
            }
    return result

# Metric display function
@app.get("/metrics")
async def metric() -> str:
    """
    Docstring for metric
    
    :return: Retruns a string of total number of operation
    :rtype: str
    """
    return Response(content=generate_latest(), media_type=CONTENT_TYPE_LATEST)

# Main
if __name__ == "__main__":
    #print(add.__doc__)
    #print(sub.__doc__)
    uvicorn.run(app, host="0.0.0.0", port=8000)