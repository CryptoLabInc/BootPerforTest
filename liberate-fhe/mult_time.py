from liberate import fhe
from liberate.fhe import presets

import time

# Generate CKKS engine with preset parameters
grade = "gold"
params = presets.params[grade]

engine = fhe.ckks_engine(**params, verbose=True)

# Generate Keys
sk = engine.create_secret_key()
pk = engine.create_public_key(sk)
evk = engine.create_evk(sk)

# Generate test data
m0 = engine.example(-1, 1)
m1 = engine.example(-10, 10)

# encode & encrypt data
ct0 = engine.encorypt(m0, pk, 1)
ct1 = engine.encorypt(m1, pk, 1)

start = time.process_time()

for i in range(1000):
    ct_mult = engine.cc_mult(ct0, ct1, evk)

end = time.process_time()

print(f"time : {int(round((end - start) * 1000))}ms")


# decrypt & decode data
result_decrypted = engine.decrode(ct_mult, sk)

