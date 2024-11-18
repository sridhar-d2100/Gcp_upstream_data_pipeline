

# **GCP Upstream Data Pipeline** 🚀  
![Python](https://img.shields.io/badge/Python-3.x-blue.svg?logo=python)  
![Apache Spark](https://img.shields.io/badge/Apache%20Spark-3.x-orange.svg?logo=apachespark)  
![Apache Airflow](https://img.shields.io/badge/Apache%20Airflow-2.x-blue.svg?logo=apacheairflow)  
![Tekton](https://img.shields.io/badge/Tekton-Pipeline-red.svg?logo=tekton)  

A scalable and robust data pipeline that uses **Google Cloud Platform (GCP)** for deployment, integrates various upstream data sources, and processes data using **Apache Spark**. Automation is achieved with **Apache Airflow** and **Tekton Pipelines**.  

---

## **✨ Key Features**  

### 🔗 **Data Collection**  
1. **Backend Systems**:  
   - Collect data via HTTP GET requests.  
   - Process the data using Spark DataFrames.  
  
2. **Microsoft SQL Server**:  
   - Connect and fetch data using **Spark JDBC**.  
 
3. **Static Files**:  
   - Read files stored in drives with Spark.  

4. **Real-Time Data**:  
   - Consume streams using **Kafka**.  

---



## **⚙️ Deployment Workflow**  

### 🛠️ **Step 1: Code Updates**  
- Push code to **GitHub**.  
- Trigger the pipeline automatically upon:  
  1. Changes in the **PySpark code**.  
  2. Updates to **Airflow DAG tasks**.  

### 📋 **Step 2: Workflow Execution**  
- **Apache Airflow**: Schedules and triggers workflows.  
- **Tekton Pipelines**: Manages CI/CD with YAML-based configurations.  


---

## **🔧 Technologies Used**  
| Tool/Platform       | Purpose                          |  
|---------------------|----------------------------------|  
| **Google Cloud Platform** | Cloud deployment and scaling |  
| **Apache Spark**        | Data processing and transformation |  
| **Apache Airflow**      | Workflow orchestration        |  
| **Tekton Pipelines**    | CI/CD automation              |  
| **Kafka**               | Real-time data streaming      |  

---



## **🚀 Get Started**  
1. Clone the repository:  
   ```bash
   git clone https://github.com/username/GCP_Upstream_Data_Pipeline.git
   cd GCP_Upstream_Data_Pipeline
   ```  
2. Install dependencies and follow the setup guide.  
3. Push changes to GitHub to trigger the pipeline.  

---

