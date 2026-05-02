import datetime
from google.adk.agents import Agent

def analyze_catch(hold_time: float, ball_touched_ground: bool) -> dict:
    """
    Determine whether a cricket catch is valid based on hold time and ground contact.

    Args:
        hold_time (float): The amount of time in seconds the fielder controlled the ball.
        ball_touched_ground (bool): Whether the ball touched the ground before or during the catch.

    Returns:
        dict: A dictionary containing:
            - status (str): 'success'
            - decision (str): 'OUT' or 'NOT OUT'
            - reason (str): Explanation for the decision
    """
    if ball_touched_ground:
        return {
            "status": "success",
            "decision": "NOT OUT",
            "reason": "The ball touched the ground."
        }
    
    if hold_time < 1.0:
        return {
            "status": "success",
            "decision": "NOT OUT",
            "reason": f"Hold time of {hold_time}s is less than the required 1.0s."
        }
        
    return {
        "status": "success",
        "decision": "OUT",
        "reason": "Valid catch. Fielder had control for sufficient time and ball did not touch the ground."
    }

root_agent = Agent(
    model="gemini-flash-latest",
    name="catch_validity_agent",
    description="Agent that analyzes whether a cricket catch is valid based on hold time and ground contact.",
    instruction="You are an intelligent cricket decision assistant. Use the analyze_catch tool to determine whether a catch is OUT or NOT OUT. Always explain the reasoning clearly and concisely.",
    tools=[analyze_catch]
)
