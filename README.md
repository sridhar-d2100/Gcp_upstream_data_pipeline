
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
   - ![HTTP Icon](https://img.icons8.com/color/48/null/http.png)  

2. **Microsoft SQL Server**:  
   - Connect and fetch data using **Spark JDBC**.  
   - ![SQL Icon](https://img.icons8.com/color/48/null/database.png)  

3. **Static Files**:  
   - Read files stored in drives with Spark.  
   - ![File Icon](https://img.icons8.com/color/48/null/file.png)  

4. **Real-Time Data**:  
   - Consume streams using **Kafka**.  
   - ![Kafka Icon](https://img.icons8.com/color/48/null/streaming.png)  

---

### 📂 **Supported File Formats**  
| Format  | Example Use Cases |  
|---------|-------------------|  
| 🟢 JSON  | API responses, logs |  
| 🟡 XML   | Legacy systems, configurations |  
| 🔵 CSV   | Tabular data, reports |  
| 🟣 XLSX  | Excel sheets |  
| 🟠 Parquet | Big data storage, analytics |  

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

![Pipeline Workflow](https://via.placeholder.com/800x400.png?text=Insert+Pipeline+Image+Here)  

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

## **📊 Example Output**  
Here’s a sample of what the pipeline processes:  

```json
{
  "job_id": "12345",
  "source": "SQL Server",
  "file_type": "CSV",
  "status": "Processed",
  "rows_ingested": 100000
}
```

---

### **📸 Visual Overview**  
![Visual Diagram](https://via.placeholder.com/800x400.png?text=Insert+Pipeline+Architecture+Diagram+Here)  

---

## **🚀 Get Started**  
1. Clone the repository:  
   ```bash
   git clone https://github.com/username/GCP_Upstream_Data_Pipeline.git
   cd GCP_Upstream_Data_Pipeline
   ```  
2. Install dependencies and follow the setup guide.  
3. Push changes to GitHub to trigger the pipeline.  
