"""
Gemini Service - AI-powered explanations
Optional: Requires GEMINI_API_KEY in .env
"""
import os
from typing import List, Dict, Any

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")


def explain_reorders(reorder_items: List[Dict[str, Any]]) -> str:
    """
    Generate AI explanation for reorder suggestions using Gemini
    Falls back to simple explanation if API not available
    """
    
    # Agar API key nahi hai to simple explanation de do
    if not GEMINI_API_KEY:
        return _simple_explanation(reorder_items)
    
    try:
        # Gemini API call karna chahte ho to yahan add kro
        # For now, simple explanation return kar rahe hain
        return _simple_explanation(reorder_items)
    
    except Exception as e:
        # Agar error aaye to fallback
        return _simple_explanation(reorder_items)


def _simple_explanation(items: List[Dict[str, Any]]) -> str:
    """
    Simple text-based explanation without Gemini API
    """
    if not items:
        return "Koi product reorder ke liye ready nahi hai."
    
    explanation = f"**Reorder Suggestions ({len(items)} items):**\n\n"
    
    for i, item in enumerate(items, 1):
        name = item.get('product_name', 'Unknown')
        stock = item.get('current_stock', 0)
        suggested = item.get('suggested_order_qty', 0)
        daily_sales = item.get('average_daily_sales', 0)
        
        explanation += f"{i}. **{name}**\n"
        explanation += f"   - Current Stock: {stock} units\n"
        explanation += f"   - Daily Sales: {daily_sales:.1f} units/day\n"
        explanation += f"   - Suggested Order: {int(suggested)} units\n"
        explanation += f"   - Status: URGENT REORDER\n\n"
    
    explanation += "✅ In sabhi products ko jaldi order karna chahiye takey stock out na ho!"
    return explanation