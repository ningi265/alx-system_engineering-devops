# Postmortem Report

## Issue Summary
**Duration of Outage:**  
- **Start Time:** August 15, 2024, 2:00 PM GMT  
- **End Time:** August 15, 2024, 4:00 PM GMT

**Impact:**  
- The main e-commerce service was down, leading to significant disruptions. Users were unable to place orders or browse products during this period.
- **User Impact:** Approximately 80% of the users were affected, particularly those attempting to make purchases or access their shopping carts.

**Root Cause:**  
- A misconfiguration in the Nginx server caused a failure in routing requests properly, leading to service downtime.

## Timeline
- **2:00 PM GMT:** Monitoring alert detected a spike in error rates across the e-commerce application.
- **2:05 PM GMT:** The on-call engineer received an alert and began investigating the issue. 
- **2:10 PM GMT:** Initial assumption was that the database was overloaded due to traffic spikes.
- **2:15 PM GMT:** Checked database logs and performance metrics; no significant issues detected.
- **2:25 PM GMT:** Investigated the application server, but no clear cause was found.
- **2:35 PM GMT:** Realized that the issue might be with the Nginx server configuration.
- **2:45 PM GMT:** Discovered a misconfigured Nginx directive that was preventing proper routing.
- **2:50 PM GMT:** Escalated the issue to the DevOps team.
- **3:00 PM GMT:** The DevOps team corrected the Nginx configuration and restarted the server.
- **3:15 PM GMT:** Monitoring confirmed that the service was beginning to stabilize.
- **4:00 PM GMT:** All services fully restored and functioning normally.

## Root Cause and Resolution
**Root Cause:**  
- The root cause was a misconfiguration in the Nginx server. A directive responsible for routing requests to the correct upstream servers was incorrectly set, leading to 502 Bad Gateway errors.

**Resolution:**  
- The configuration file was corrected by updating the directive to properly map requests to the correct upstream servers. Once the configuration was fixed, the Nginx server was restarted, restoring normal operations.

## Corrective and Preventative Measures
**Improvements:**  
- Improve the configuration review process to ensure all changes are peer-reviewed.
- Enhance monitoring and alerts to catch configuration errors before they cause widespread outages.
- Implement a staging environment where configuration changes can be tested before being deployed to production.

**Tasks:**
- [ ] Patch Nginx server configuration and deploy the corrected version.
- [ ] Add automated tests to validate critical server configurations.
- [ ] Implement detailed logging for configuration changes to track future issues.
- [ ] Enhance monitoring tools to include configuration validation.
- [ ] Conduct training for team members on proper Nginx configuration management.

## Repository
This postmortem is part of the `alx-system_engineering-devops` repository.

**Directory:** `0x19-postmortem`  
**File:** `README.md`

