#!/usr/bin/env python3
"""
Bright Data vs Webshare Proxy Cost Comparison Calculator 2026.
Analyzes residential bandwidth expenses and volume discounts.
"""
import argparse

def compare_proxies(volume_gb, brightdata_rate, webshare_rate):
    brightdata_cost = volume_gb * brightdata_rate
    webshare_cost = volume_gb * webshare_rate
    monthly_savings = brightdata_cost - webshare_cost
    annual_savings = monthly_savings * 12.0
    return {
        "brightdata_cost": brightdata_cost,
        "webshare_cost": webshare_cost,
        "monthly_savings": monthly_savings,
        "annual_savings": annual_savings
    }

def main():
    parser = argparse.ArgumentParser(description="Bright Data vs Webshare Cost Benchmark")
    parser.add_argument("--volume-gb", type=float, default=60.0, help="Monthly bandwidth in GB (default: 60)")
    parser.add_argument("--bright-rate", type=float, default=8.40, help="Bright Data per-GB rate (default: $8.40)")
    parser.add_argument("--webshare-rate", type=float, default=3.50, help="Webshare residential per-GB rate (default: $3.50)")
    args = parser.parse_args()

    res = compare_proxies(args.volume_gb, args.bright_rate, args.webshare_rate)
    print(f"Monthly Volume:          {args.volume_gb:.0f} GB")
    print(f"Bright Data (@${args.bright_rate:.2f}/GB): ${res['brightdata_cost']:.2f}/mo")
    print(f"Webshare (@${args.webshare_rate:.2f}/GB):    ${res['webshare_cost']:.2f}/mo")
    print(f"Monthly Net Savings:     ${res['monthly_savings']:.2f}/mo")
    print(f"Annual Projected Savings:${res['annual_savings']:.2f}/year")

if __name__ == "__main__":
    main()
