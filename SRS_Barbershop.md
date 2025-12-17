# ระบบบริหารจัดการร้านตัดผม
## Software Requirement Specification Document

**เวอร์ชัน:** 1.0  
**วันที่:** 17 ธันวาคม 2024  
**จัดทำโดย:** ทีมพัฒนาระบบบริหารจัดการร้านตัดผม

---

## ประวัติการจัดทำเอกสาร

| วันที่ | เวอร์ชัน | รายละเอียดการเปลี่ยนแปลง | ผู้ดำเนินการ |
|-------|----------|------------------------|------------|
| 17/12/2024 | 1.0 | จัดทำเอกสารฉบับแรก | ทีมพัฒนา |

---

## สารบัญ
1. [Introduction](#1-introduction)
   - 1.1 วัตถุประสงค์
   - 1.2 ภาพรวมของระบบ
   - 1.3 ขอบเขต
   - 1.4 กลุ่มผู้ใช้งาน

2. [System Requirements](#2-system-requirements)
   - 2.1 Hardware Requirements
   - 2.2 Software Requirements
   - 2.3 External Interfaces

3. [Software Requirements](#3-software-requirements)
   - 3.1 ระบบสมาชิกและลูกค้าสัมพันธ์ (CRM)
   - 3.2 ระบบจองคิวและบริหารจัดการคิว
   - 3.3 ระบบชำระเงินและจุดขาย (POS)
   - 3.4 ระบบบริหารจัดการช่างและตารางงาน
   - 3.5 ระบบจัดการสต็อกสินค้าและบริการ
   - 3.6 ระบบรายงานและผู้ดูแลระบบ

4. [Non-Functional Requirements](#4-non-functional-requirements)
   - 4.1 Performance Requirements
   - 4.2 Security Requirements
   - 4.3 Usability Requirements
   - 4.4 Reliability Requirements
   - 4.5 Maintainability Requirements

---

## 1. Introduction

### 1.1 วัตถุประสงค์
- เพื่อพัฒนาระบบบริหารจัดการร้านตัดผมที่มีประสิทธิภาพครบวงจร
- เพื่ออำนวยความสะดวกในการจองคิวออนไลน์และการจัดการคิวหน้าร้าน
- เพื่อเพิ่มประสิทธิภาพในการบริหารจัดการข้อมูลลูกค้า ประวัติทรงผม และสต็อกสินค้า

### 1.2 ภาพรวมของระบบ
ระบบบริหารจัดการร้านตัดผมเป็นแพลตฟอร์มที่พัฒนาขึ้นเพื่อรองรับการดำเนินงานของร้านตัดผมสมัยใหม่ โดยเชื่อมโยงการทำงานระหว่างส่วนหน้าบ้าน (Front-end) สำหรับลูกค้าและช่างตัดผม และส่วนหลังบ้าน (Back-end) สำหรับผู้บริหาร ระบบครอบคลุมตั้งแต่วิเคราะห์คิว การให้บริการ การชำระเงิน ไปจนถึงการเก็บข้อมูลประวัติทรงผมเพื่อการบริการที่ดียิ่งขึ้น

ระบบงานประกอบด้วยส่วนสำคัญดังนี้:
1. ระบบสมาชิก - จัดการข้อมูลลูกค้า ประวัติการตัดผม และระบบสะสมแต้ม
2. ระบบจองคิว - รองรับการจองผ่านเว็บ/แอป และการจัดการ Walk-in หน้าร้าน
3. ระบบ POS - คำนวณค่าบริการ ตัดสต็อกสินค้า และออกใบเสร็จ
4. ระบบจัดการช่าง - บริหารตารางงานและคำนวณค่าคอมมิชชั่น
5. ระบบรายงาน - สรุปยอดขายและประสิทธิภาพการทำงาน

### 1.3 ขอบเขต
- ระบบรองรับการจองคิวออนไลน์และ Walk-in
- ระบบจัดการข้อมูลลูกค้าและประวัติทรงผม (รูปภาพ)
- ระบบจัดการการเงินและสินค้าคงคลัง
- ระบบรายงานและสถิติเชิงลึก

### 1.4 กลุ่มผู้ใช้งาน
1. ลูกค้า
   - ลูกค้าทั่วไป (Walk-in)
   - สมาชิก (Member)
2. เจ้าหน้าที่ร้าน
   - ช่างตัดผม (Barber/Stylist)
   - พนักงานต้อนรับ/แคชเชียร์
3. ผู้ดูแลระบบ/เจ้าของร้าน

---

## 2. System Requirements

### 2.1 Hardware Requirements
- Server Requirements:
  - CPU: 4 Cores หรือสูงกว่า
  - RAM: 16GB ขึ้นไป
  - Storage: SSD 500GB ขึ้นไป (รองรับการจัดเก็บไฟล์รูปภาพจำนวนมาก)

- Client Requirements (หน้าร้าน):
  - POS Terminal หรือ Computer/Tablet
  - เครื่องพิมพ์ใบเสร็จ (Thermal Printer)
  - เครื่องอ่านบาร์โค้ด (Barcode Scanner)
  - จอแสดงผลสถานะคิว (Smart TV/Monitor)

### 2.2 Software Requirements
- Operating System: Linux Server (Ubuntu/CentOS)
- Web Server: Nginx หรือ Apache
- Database: PostgreSQL หรือ MySQL 8.0 ขึ้นไป
- Programming Language: Node.js หรือ Python

### 2.3 External Interfaces

#### 2.3.1 User Interfaces
| Interface ID | Description | Platform/Technology |
|-------------|-------------|-------------------|
| UI-01 | หน้าเว็บไซต์/แอปสำหรับลูกค้าจองคิว | Web Browser/Mobile App |
| UI-02 | หน้าจัดการระบบและ POS สำหรับเจ้าหน้าที่ | Web Browser/Tablet |
| UI-03 | หน้าจอแสดงลำดับคิวในร้าน | TV Browser |

#### 2.3.2 Hardware Interfaces
| Interface ID | Description | Protocol |
|-------------|-------------|----------|
| HW-01 | เครื่องพิมพ์ใบเสร็จความร้อน | USB/LAN |
| HW-02 | ลิ้นชักเก็บเงิน | RJ11 |
| HW-03 | เครื่องสแกน QR Code/Barcode | USB/Bluetooth |

#### 2.3.3 Software Interfaces
| Interface ID | Description | Protocol/API |
|-------------|-------------|--------------|
| SW-01 | ระบบชำระเงินออนไลน์ (Payment Gateway) | REST API |
| SW-02 | ระบบส่ง SMS แจ้งเตือน | SMS Gateway API |
| SW-03 | LINE Official Account (Rich Menu/Notify) | LINE Messaging API |
| SW-04 | Google Maps (แสดงที่ตั้งสาขา) | Google Maps API |

#### 2.3.4 Communication Interfaces
| Interface ID | Description | Protocol |
|-------------|-------------|----------|
| COM-01 | การเชื่อมต่อกับระบบ PromptPay | HTTPS/SSL |
| COM-02 | การแจ้งเตือนสถานะคิว | WebSocket |

---

## 3. Software Requirements

### 3.1 ระบบสมาชิกและลูกค้าสัมพันธ์ (CRM)

| Requirement ID | Requirement Description | Priority |
|---------------|------------------------|----------|
| MEM-01 | ระบบต้องรองรับการบันทึกข้อมูลลูกค้า:<br>- ชื่อ-นามสกุล<br>- เบอร์โทรศัพท์ (ใช้เป็น User ID)<br>- วันเกิด<br>- รูปถ่าย<br>- ช่องทางติดต่อ (LINE ID) | High |
| MEM-02 | ระบบต้องบันทึกประวัติทรงผม:<br>- รูปถ่าย Before/After<br>- รายละเอียดทรงที่ตัด<br>- ช่างที่ให้บริการ<br>- วันที่ใช้บริการ | High |
| MEM-03 | ระบบต้องรองรับระบบสมาชิกแบบระดับ (Tier):<br>- Bronze, Silver, Gold, Platinum<br>- การเลื่อนระดับอัตโนมัติตามยอดใช้จ่าย | Medium |
| MEM-04 | ระบบต้องรองรับการสะสมและแลกแต้ม:<br>- 1 บาท = 1 แต้ม<br>- แต้มพิเศษวันเกิด (x2)<br>- แลกแต้มเป็นส่วนลด | High |
| MEM-05 | ระบบต้องแสดงประวัติการเข้าใช้บริการย้อนหลังได้ | Medium |

### 3.2 ระบบจองคิวและบริหารจัดการคิว (Booking & Queue)

| Requirement ID | Requirement Description | Priority |
|---------------|------------------------|----------|
| BKG-01 | ระบบต้องรองรับการจองคิวผ่านช่องทาง:<br>- เว็บไซต์/แอปพลิเคชัน<br>- LINE Official<br>- หน้าร้าน (Walk-in) | High |
| BKG-02 | ระบบต้องตรวจสอบสถานะช่างว่างแบบ Real-time ก่อนยืนยันการจอง | High |
| BKG-03 | ระบบต้องออกรหัสการจอง (Booking ID/QR Code) ให้ลูกค้า | High |
| BKG-04 | ระบบต้องคำนวณเวลารอโดยประมาณสำหรับลูกค้า Walk-in | High |
| BKG-05 | ระบบต้องมีการแจ้งเตือน:<br>- ก่อนถึงเวลานัด 1 ชม.<br>- เมื่อถึงคิว<br>- เมื่อช่างพร้อมให้บริการ | High |
| BKG-06 | ระบบต้องแสดงสถานะคิวบนหน้าจอ TV ในร้าน (รอคิว, กำลังตัด, เสร็จสิ้น) | Medium |

### 3.3 ระบบชำระเงินและจุดขาย (POS System)

| Requirement ID | Requirement Description | Priority |
|---------------|------------------------|----------|
| POS-01 | ระบบต้องรองรับการชำระเงินผ่าน:<br>- เงินสด<br>- QR Payment<br>- บัตรเครดิต<br>- แต้มสะสม | High |
| POS-02 | ระบบต้องคำนวณยอดรวมสุทธิ:<br>- ค่าบริการ + ค่าสินค้า<br>- หักส่วนลดสมาชิก/คูปอง<br>- คำนวณ VAT (ถ้ามี) | High |
| POS-03 | ระบบต้องออกใบเสร็จรับเงิน/ใบกำกับภาษีอย่างย่อและเต็มรูป | High |
| POS-04 | ระบบต้องรองรับการขายสินค้าหน้าร้าน (ตัดสต็อกทันที) | High |

### 3.4 ระบบบริหารจัดการช่างและตารางงาน (Staff Management)

| Requirement ID | Requirement Description | Priority |
|---------------|------------------------|----------|
| STF-01 | ระบบต้องจัดการข้อมูลช่างตัดผม:<br>- ประวัติและรูปถ่าย<br>- ความเชี่ยวชาญ<br>- สถานะการทำงาน (ว่าง/ติดลูกค้า/พัก) | High |
| STF-02 | ระบบต้องจัดการตารางงาน (Shift Management):<br>- วันทำงาน/วันหยุด<br>- เวลาพักเบรค | High |
| STF-03 | ระบบต้องคำนวณค่าคอมมิชชั่นของช่างตามยอดบริการ | High |
| STF-04 | ระบบต้องมี Dashboard สำหรับช่างเพื่อดูคิวงานของตนเอง | Medium |

### 3.5 ระบบจัดการสต็อกสินค้าและบริการ (Inventory & Service)

| Requirement ID | Requirement Description | Priority |
|---------------|------------------------|----------|
| INV-01 | ระบบต้องจัดการข้อมูลบริการ:<br>- ราคาตามระดับช่าง<br>- ราคาตามความยาวผม<br>- ระยะเวลาที่ใช้โดยประมาณ | High |
| INV-02 | ระบบต้องจัดการสินค้าคงคลัง:<br>- รับสินค้าเข้า<br>- ตัดสินค้าออกเมื่อขายหรือใช้ในร้าน<br>- แจ้งเตือนเมื่อสินค้าใกล้หมด | High |
| INV-03 | ระบบต้องรองรับการจัดโปรโมชันและแพ็คเกจ (เช่น ตัด+สระ) | Medium |

### 3.6 ระบบรายงานและผู้ดูแลระบบ (Admin & Reports)

| Requirement ID | Requirement Description | Priority |
|---------------|------------------------|----------|
| ADM-01 | ระบบต้องแสดง Dashboard ผู้บริหาร:<br>- ยอดขายรายวัน/เดือน<br>- จำนวนลูกค้า<br>- ประสิทธิภาพช่าง | High |
| ADM-02 | ระบบต้องออกรายงานทางการเงิน:<br>- รายรับ-รายจ่าย<br>- รายงานภาษี<br>- รายงานค่าคอมมิชชั่น | High |
| ADM-03 | ระบบต้องจัดการสิทธิ์ผู้ใช้งาน (Admin, Manager, Staff) | High |

---

## 4. Non-Functional Requirements

### 4.1 Performance Requirements

| Requirement ID | Requirement Description | Metric |
|---------------|------------------------|---------|
| PRF-01 | ระบบต้องรองรับผู้ใช้งานพร้อมกัน | ≥ 100 users |
| PRF-02 | เวลาตอบสนองการตรวจสอบคิวว่าง | ≤ 2 วินาที |
| PRF-03 | เวลาประมวลผลการชำระเงินและตัดสต็อก | ≤ 3 วินาที |
| PRF-04 | การอัพเดตหน้าจอคิว (Latency) | Real-time (< 1s) |

### 4.2 Security Requirements

| Requirement ID | Requirement Description | Priority |
|---------------|------------------------|----------|
| SEC-01 | การเข้ารหัสข้อมูลส่วนบุคคล (PDPA Compliance) | High |
| SEC-02 | การกำหนดสิทธิ์เข้าถึงข้อมูลตามระดับผู้ใช้ (Role-based Access) | High |
| SEC-03 | ระบบบันทึกประวัติการใช้งาน (Audit Log) | High |
| SEC-04 | Session Timeout เมื่อไม่มีการใช้งาน 30 นาที | Medium |

### 4.3 Usability Requirements

| Requirement ID | Requirement Description | Priority |
|---------------|------------------------|----------|
| USB-01 | ส่วนติดต่อผู้ใช้ (UI) ต้องใช้งานง่าย รองรับภาษาไทย | High |
| USB-02 | รองรับ Responsive Design (PC, Tablet, Mobile) | High |
| USB-03 | ระบบ POS ต้องออกแบบให้กดง่ายและรวดเร็ว | High |
| USB-04 | มีคู่มือการใช้งานออนไลน์สำหรับพนักงาน | Medium |

### 4.4 Reliability Requirements

| Requirement ID | Requirement Description | Metric |
|---------------|------------------------|---------|
| REL-01 | System Uptime | 99.5% |
| REL-02 | ระบบสำรองข้อมูลอัตโนมัติ (Daily Backup) | ทุก 24 ชั่วโมง |
| REL-03 | ระยะเวลาในการกู้คืนระบบ | ≤ 2 ชั่วโมง |
| REL-04 | รองรับโหมด Offline สำหรับ POS (กรณีเน็ตหลุด) | บันทึกในเครื่อง |

### 4.5 Maintainability Requirements

| Requirement ID | Requirement Description | Priority |
|---------------|------------------------|----------|
| MNT-01 | มีเอกสารประกอบการพัฒนาระบบ (Technical Doc) | High |
| MNT-02 | โค้ดมีการจัดการเป็นโมดูล (Modular Design) ง่ายต่อการแก้ไข | High |
| MNT-03 | รองรับการขยายสาขาในอนาคต (Scalability) | High |