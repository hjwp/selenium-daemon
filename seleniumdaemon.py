import json
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from selenium.webdriver.firefox.remote_connection import FirefoxRemoteConnection
from selenium.webdriver.remote.command import Command

class ReattachingRemoteWebDriver(RemoteWebDriver):

    def __init__(self, url, session_id, remote_capabilities):
        executor = FirefoxRemoteConnection(remote_server_addr=url)
        self._session_id = session_id
        self._remote_capabilities = remote_capabilities
        super().__init__(command_executor=executor)

    def execute(self, cmd, *args, **kwargs):
        if cmd == Command.NEW_SESSION:
            return {
                'sessionId': self._session_id,
                'capabilities': self._remote_capabilities,
            }
        return super().execute(cmd, *args, **kwargs)


def attach_to_driver():
    with open('/tmp/selenium-daemon.url') as f:
        url, session_id, json_caps = f.read().strip().split('\n')
    remote_capabilities = json.loads(json_caps)
    print('attaching to', url, session_id)
    d2 = ReattachingRemoteWebDriver(
        url=url,
        session_id=session_id,
        remote_capabilities=remote_capabilities,
    )
    d2.session_id = session_id
    return d2

