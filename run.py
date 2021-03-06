#!/usr/bin/env python
import os
from muselon import muselon
from gevent import monkey
from socketio.server import SocketIOServer


#if __name__ == '__main__':
#    port = int(os.environ.get('PORT', 5000))
#    muselon.run(host='0.0.0.0', port=port, debug=True)
    

monkey.patch_all()

# muselon.debug=True

if __name__ == '__main__':
	muselon.debug = True
	port = int(os.environ.get('PORT', 5000))
	print 'Listening on http://127.0.0.1:%s and on port 10843 (flash policy server)' % port
	SocketIOServer(('', port), muselon, resource="socket.io").serve_forever()
