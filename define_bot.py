#!/usr/bin/env python3
"""Discord dictionary and thesaurus bot"""
import argparse
def main():
 p=argparse.ArgumentParser(description="Discord dictionary and thesaurus bot")
 p.add_argument("--version",action="store_true")
 args=p.parse_args()
 if args.version:print("define-bot v0.1.0");return
 print(f"[12:13] define-bot ready")
if __name__=="__main__":main()
