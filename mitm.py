from mitmproxy.tools.main import mitmdump
import argparse

def main():
    parser = argparse.ArgumentParser(description='Run mitmdump with dynamic parameters.')
    parser.add_argument('-p', '--port', type=str, default='65000', help='Proxy Port (default: 65000)')
    parser.add_argument('-s', '--script', type=str, help='Path to the mitmproxy script.')
    parser.add_argument('-f', '--file', type=str, help='Path to the credentials.json.')
    args = parser.parse_args()

    command = ["-p", args.port]
    if args.script:
        command.extend(["-s", args.script])
    if args.file:
        command.extend(["--set", "credentials=" + args.file])

    mitmdump(command)

if __name__ == '__main__':
    main()
