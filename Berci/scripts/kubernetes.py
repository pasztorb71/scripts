"""
kubectl -n mlff-1 get pods
kubectl -n mlff-1 get pods doc-document-service-doc-step-1-d5hx2
kubectl -n mlff-1 describe pods doc-document-service-doc-step-1-d5hx2
kubectl -n mlff-1 log pods doc-document-service-doc-step-1-d5hx2
"""
projects = ['cantas-dev-s-1'
,'cantas-s-1'
,'cantas-test-s-1'
,'cantas-train-s-1'
,'mlff-dev-s'
,'mlff-fit-s'
,'mlff-perf-s'
,'mlff-sb-s']

lines = """cantas-dev-s-1-k8s  asia-southeast2  1.27.7-gke.1121000  34.128.98.248  n2-standard-8  1.27.7-gke.1121000  28         RUNNING
cantas-s-1-k8s  asia-southeast2  1.25.15-gke.1115000  34.101.92.88  e2-standard-8  1.25.15-gke.1115000  64         RUNNING
cantas-test-s-1-k8s  asia-southeast2  1.27.7-gke.1121000  34.101.227.135  e2-standard-8  1.27.7-gke.1121000  15         RUNNING
cantas-train-s-1-k8s  asia-southeast2  1.27.7-gke.1121000  34.128.105.226  e2-standard-4  1.27.7-gke.1056000 *  24         RUNNING
mlff-dev-s-k8s  europe-west1  1.25.15-gke.1115000  35.241.141.192  e2-standard-4  1.25.15-gke.1115000  14         RUNNING
mlff-fit-s-k8s  europe-west1  1.25.15-gke.1115000  34.79.221.78  e2-standard-4  1.25.15-gke.1115000  15         RUNNING
mlff-perf-s-k8s  europe-west1  1.25.15-gke.1115000  35.205.207.68  e2-standard-8  1.25.13-gke.200 *  16         RUNNING
mlff-sb-s-k8s  europe-west1  1.25.15-gke.1115000  104.155.84.28  e2-standard-8  1.25.13-gke.200 *  19         RUNNING"""

def f1():
    print(projects)
    for p in projects[0:]:
        print(f'gcloud config set project {p}')
        print(f'gcloud container clusters list')

if __name__ == '__main__':
    for idx, i in enumerate(lines.split('RUNNING')[0:-1]):
        l = i.replace('\n', '')
        arr = l.split('  ')
        print(f'gcloud config set project {projects[idx]}')
        print(f'gcloud container clusters get-credentials {arr[0]} --zone={arr[1]}')
