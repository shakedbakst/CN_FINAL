from dnslib import DNSRecord,DNSQuestion,QTYPE

MY_DNS_HOST="localhost"
MY_DNS_PORT=8053

def my_dns_query(host=MY_DNS_HOST, port=MY_DNS_PORT, query_domain="localhost"):
    question = DNSRecord(q=DNSQuestion(query_domain ,getattr(QTYPE,'A')))
    packet = bytearray(question.send(MY_DNS_HOST, MY_DNS_PORT, tcp=True))
    original = DNSRecord.parse(packet)
    query_ip = original.rr[0].rdata
    return query_ip