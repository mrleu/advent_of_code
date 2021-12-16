import math


class Packet:
    def get_num(self, n):
        return int(self.get_bits(n), 2)

    def get_bits(self, n):
        self.packet_len += n
        return "".join(next(self.data) for _ in range(n))

    def version_sum(self):
        return self.version + sum(x.version_sum() for x in self.subpackets)

    def __init__(self, data):
        if isinstance(data, str):
            hex_len = len(data)
            data = bin(int(data, 16))[2:].zfill(4 * hex_len)
            self.data = iter(data)
        else:
            self.data = iter(data)
        self.subpackets = []
        self.packet_len = 0
        self.version = self.get_num(3)
        self.type_id = self.get_num(3)

        if self.type_id == 4:
            num = ""
            while True:
                d = self.get_bits(5)
                num += d[1:]
                if d[0] == "0":
                    break
            self.value = int(num, 2)
        else:
            if self.get_bits(1) == "0":
                plen = self.get_num(15)
                while plen > 0:
                    self.subpackets.append(Packet(self.data))
                    self.packet_len += self.subpackets[-1].packet_len
                    plen -= self.subpackets[-1].packet_len
            else:
                pcount = self.get_num(11)
                for _ in range(pcount):
                    self.subpackets.append(Packet(self.data))
                    self.packet_len += self.subpackets[-1].packet_len

    def __repr__(self):
        if self.subpackets:
            return f"Packet(version={self.version}, type_id={self.type_id}, subpackets={self.subpackets})"
        else:
            return f"Packet(version={self.version}, type_id={self.type_id}, value={self.value})"

    def eval(self):
        if self.type_id == 0:
            return sum(x.eval() for x in self.subpackets)
        elif self.type_id == 1:
            return math.prod(x.eval() for x in self.subpackets)
        elif self.type_id == 2:
            return min(x.eval() for x in self.subpackets)
        elif self.type_id == 3:
            return max(x.eval() for x in self.subpackets)
        elif self.type_id == 4:
            return self.value
        assert len(self.subpackets) == 2
        if self.type_id == 5:
            return int(self.subpackets[0].eval() > self.subpackets[1].eval())
        elif self.type_id == 6:
            return int(self.subpackets[0].eval() < self.subpackets[1].eval())
        elif self.type_id == 7:
            return int(self.subpackets[0].eval() == self.subpackets[1].eval())
        raise ValueError(f"Invalid {self.type_id}")


line = "220D700071F39F9C6BC92D4A6713C737B3E98783004AC0169B4B99F93CFC31AC4D8A4BB89E9D654D216B80131DC0050B20043E27C1F83240086C468A311CC0188DB0BA12B00719221D3F7AF776DC5DE635094A7D2370082795A52911791ECB7EDA9CFD634BDED14030047C01498EE203931BF7256189A593005E116802D34673999A3A805126EB2B5BEEBB823CB561E9F2165492CE00E6918C011926CA005465B0BB2D85D700B675DA72DD7E9DBE377D62B27698F0D4BAD100735276B4B93C0FF002FF359F3BCFF0DC802ACC002CE3546B92FCB7590C380210523E180233FD21D0040001098ED076108002110960D45F988EB14D9D9802F232A32E802F2FDBEBA7D3B3B7FB06320132B0037700043224C5D8F2000844558C704A6FEAA800D2CFE27B921CA872003A90C6214D62DA8AA9009CF600B8803B10E144741006A1C47F85D29DCF7C9C40132680213037284B3D488640A1008A314BC3D86D9AB6492637D331003E79300012F9BDE8560F1009B32B09EC7FC0151006A0EC6082A0008744287511CC0269810987789132AC600BD802C00087C1D88D05C001088BF1BE284D298005FB1366B353798689D8A84D5194C017D005647181A931895D588E7736C6A5008200F0B802909F97B35897CFCBD9AC4A26DD880259A0037E49861F4E4349A6005CFAD180333E95281338A930EA400824981CC8A2804523AA6F5B3691CF5425B05B3D9AF8DD400F9EDA1100789800D2CBD30E32F4C3ACF52F9FF64326009D802733197392438BF22C52D5AD2D8524034E800C8B202F604008602A6CC00940256C008A9601FF8400D100240062F50038400970034003CE600C70C00F600760C00B98C563FB37CE4BD1BFA769839802F400F8C9CA79429B96E0A93FAE4A5F32201428401A8F508A1B0002131723B43400043618C2089E40143CBA748B3CE01C893C8904F4E1B2D300527AB63DA0091253929E42A53929E420"
p = Packet(line)
print(p.version_sum(), p.eval())
